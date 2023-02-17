from django import forms

# class VideoForm(forms.Form):
#     file = forms.FileField(label='Select a video (5 seconds or less):', help_text='Max. 5MB')
#     tags = forms.CharField(max_length=100, help_text='Enter up to 3 comma-separated tags like #tag1, #tag2, #tag3')
    
# class VideoForm(forms.Form):
#     file = forms.FileField(label='Select a video (5 seconds or less):', required=True, help_text='Max. 5MB')
#     tags = forms.CharField(label='Tags', required=True, help_text='Enter up to 3 comma-separated tags like #tag1, #tag2, #tag3')

#     # Customize error messages
#     error_messages = {
#         'file_type': 'The selected file must be a video file (mp4, avi, mov, or wmv)',
#         'file_size': 'The selected file must be 5 seconds or less',
#         'max_tags': 'You can only add up to 3 tags',
#         'file_req': 'Video file is required.',
#     }
    
#     def clean_file(self):
#         file = self.cleaned_data.get('file')
#         if file:
#             if file.content_type not in ['video/mp4', 'video/avi', 'video/quicktime', 'video/x-ms-wmv']:
#                 raise forms.ValidationError(self.error_messages['file_type'])
#             if file.size > 5242880:
#                 raise forms.ValidationError(self.error_messages['file_size'])
#             if not is_video(file.name):
#                 raise forms.ValidationError(self.error_messages['file_type'])
#             if get_video_duration(file) > 5:
#                 raise forms.ValidationError(self.error_messages['file_size'])
#             return file
#         else:
#             raise forms.ValidationError(self.error_messages['file_req'])

# class VideoForm(forms.Form):
#     file = forms.FileField(label='Select a video file', required=True, widget=forms.ClearableFileInput(attrs={'multiple': False}))
#     tags = forms.CharField(label='Tags', required=True, max_length=200)

#     def clean_file(self):
#         file = self.cleaned_data['file']
#         if file:
#             # Check if file is a video and less than 5 seconds long
#             content_type = file.content_type.split('/')[0]
#             if content_type != 'video':
#                 raise forms.ValidationError('File must be a video.')
#             try:
#                 from moviepy.video.io.VideoFileClip import VideoFileClip
#                 clip = VideoFileClip(file.temporary_file_path())
#                 duration = clip.duration
#                 clip.close()
#                 if duration > 5:
#                     raise forms.ValidationError('Video must be 5 seconds or less.')
#             except Exception:
#                 raise forms.ValidationError('An error occurred while processing the video file.')
#         return file
    
#     def clean_tags(self):
#         tags = self.cleaned_data['tags']
#         if tags:
#             tag_list = tags.split(',')
#         if len(tag_list) > 3:
#             raise forms.ValidationError('You can select up to 3 tags.')
#         return tags

#     def clear_tags(self):
#         self.cleaned_data['tags'] = ''
#         self.add_error('tags', '')
