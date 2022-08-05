import ftplib;

class FTP:
  
    def __init__(self, host, port, username, password ):

        self.ftp = ftplib.FTP( host )
        self.ftp.login( username, password )

    def close():
        self.ftp.quit()

    def download( file_name ):
        # Check file exists on the FTP Server.
        try:
            resp = self.ftp.sendcmd( ( "MLST " + file_name + ".csv" ) )
        except:
            # File does not exist, error handling.
            print("Error. The file specified does not exist on the server.")

        # File does exist, proceed.
        if 'type=file;' in resp:
            with open( download_path + file_name + ".csv", 'wb') as f:
                self.ftp.retrbinary('RETR ' + file_name + ".csv", f.write)
