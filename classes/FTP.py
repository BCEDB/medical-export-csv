import ftplib;

class FTP:
  
    def __init__(self, host, username, password ):

        self.ftp = ftplib.FTP( host )
        self.ftp.login( username, password )
        self.download_path = '/'

    def close( self ):
        self.ftp.quit()

    def download( self, file_name, destination_path ):
        # Check file exists on the FTP Server.
        try:
            resp = self.ftp.sendcmd( ( "MLST " + file_name + ".csv" ) )
        except:
            # File does not exist, throw a FileNotFoundError.
            raise FileNotFoundError("Error. The file specified does not exist on the server.")

        # File does exist, proceed.
        if 'type=file;' in resp:
            with open( destination_path + file_name + ".csv", 'wb') as f:
                self.ftp.retrbinary('RETR ' + file_name + ".csv", f.write)

        return destination_path + file_name + ".csv"