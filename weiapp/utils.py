import os

def is_video(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'mov', 'wmv'}
    # ext = os.path.splitext(filename)[1]
    # return ext.lower() in ['.mp4', '.avi', '.mov', '.flv', '.wmv', '.webm']
