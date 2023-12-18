


ftp_server = "access953402404.webspace-data.io"
ftp_port = 22
ftp_username = "u111406352"
ftp_password = "jidjip-sykjer-visFa"


source_path = "/./home/jovyan/work/"
target_path = "/"

def scan_directory():
    file_dict = {}
    for root, dirs, files in os.walk(source_path):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_dict[file_path] = file_size
    return file_dict

file_dict = scan_directory()
def upload_directory():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ftp_server, port=ftp_port, username=ftp_username, password=ftp_password)
    sftp = ssh.open_sftp()

    for root, dirs, files in os.walk(source_path):
        for name in dirs:
            sub_dir = os.path.join(target_path, root.replace(source_path, ''), name)
            sftp.mkdir(sub_dir)
        for file in files:
            local_path = os.path.join(root, file)
            remote_path = os.path.join(target_path, root.replace(source_path, ''), file)
            sftp.put(local_path, remote_path)
    sftp.close()
    ssh.close()

print("Lade Verzeichnis auf FTP-Server hoch...")
upload_directory()
print("Upload abgeschlossen.")
