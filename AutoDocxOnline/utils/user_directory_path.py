def user_documents_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/documents/{1}'.format(instance.owner.id, filename)
