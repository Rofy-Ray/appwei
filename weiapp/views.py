# weiapp/views.py

import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from azure.storage.blob import BlobServiceClient, ContentSettings
from azure.data.tables import TableClient, TableServiceClient, UpdateMode
from azure.cosmosdb.table import Entity


def index(request):
    if request.method == 'POST':
        vid_file = request.FILES['video']
        vid_tags = request.POST.get('tags', '')
        tag_list = [tag.strip() for tag in vid_tags.split(',') if tag.strip()]
        
        if vid_file.size > 5242880:  # 5MB = 5 * 1024 * 1024 bytes
            messages.add_message(request, messages.ERROR, 'The video file size must be 5 MB or less.', extra_tags='danger')
        elif len(tag_list) > 3:
            messages.add_message(request, messages.ERROR, 'You can only add up to 3 tags.', extra_tags='danger')
        else:
            blob_service_client = BlobServiceClient.from_connection_string(os.environ.get('AZURE_STORAGE_CONNECTION_STRING'))
            container_name = os.environ.get('AZURE_STORAGE_CONTAINER_NAME')
            container_client = blob_service_client.get_container_client(container_name)

            table_service_client = TableServiceClient.from_connection_string(os.environ.get('AZURE_TABLE_STORAGE_CONNECTION_STRING'))
            table_name = os.environ.get('AZURE_TABLE_STORAGE_TABLE_NAME')
            table_client = table_service_client.get_table_client(table_name)

            filename = os.path.basename(vid_file.name)
            blob_vid_client = container_client.get_blob_client(filename)
            blob_vid_client.upload_blob(vid_file, overwrite=True)
            
            entity = Entity()
            entity.PartitionKey = filename
            entity.RowKey = 'tags'
            entity.tags = ','.join(tag_list)
            table_client.upsert_entity(entity=entity, mode=UpdateMode.REPLACE)
                        
            messages.add_message(request, messages.SUCCESS, 'Your video upload is successful.')
        
        return render(request, 'index.html')
    
    return render(request, 'index.html')


# fs = FileSystemStorage()
# filename = fs.save(vid_file.name, vid_file)
# tags_file = os.path.splitext(filename)[0] + '_tags.txt'
# with open(os.path.join(settings.MEDIA_ROOT, tags_file), 'w') as f:
#     f.write(vid_tags)

# blob_service_client = BlobServiceClient.from_connection_string(os.environ.get('AZURE_STORAGE_CONNECTION_STRING'))
# container_name = os.environ.get('AZURE_STORAGE_CONTAINER_NAME')
# container_client = blob_service_client.get_container_client(container_name)

# filename = os.path.basename(vid_file.name)
# blob_vid_client = container_client.get_blob_client(filename)
# blob_vid_client.upload_blob(vid_file, overwrite=True)

# tags_file = os.path.splitext(filename)[0] + '_tags.txt'
# blob_tags_client = container_client.get_blob_client(tags_file)
# blob_tags_client.upload_blob(vid_tags, overwrite=True)
