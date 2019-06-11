#!/usr/bin/python3
import contextlib
from tempfile import NamedTemporaryFile

from OpenSSL import crypto


dire ="temp\\"


@contextlib.contextmanager
def pfx_to_pem(pfx_path, pfx_password):

    with NamedTemporaryFile(suffix=".pem", dir=dire, delete=False) as f_pem:
        pfx = open(pfx_path, 'rb').read()

        p12 = crypto.load_pkcs12(pfx, pfx_password)
        f_pem.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()))
        f_pem.write(crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate()))
        ca = p12.get_ca_certificates()
        if ca is not None:
            for cert in ca:
                f_pem.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        f_pem.close()
        yield f_pem.name


#
