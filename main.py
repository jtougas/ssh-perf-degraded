import cryptography
import logging
from cryptography.hazmat.primitives.asymmetric import dh
def main():
    root = logging.getLogger()
    root.setLevel("DEBUG")

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
    root.addHandler(sh)

    
    peer_public = 21219076387477973597947551210743057558749877688782906377828784897690962480179550649790103475250548770738743764986393421549635080648006559292990134342760337339134652460561074016620314689583003349767391714258237037594222313730450522095033576031458518933050215765694798313011125039273060674683856697289212376856222579162385248218612784912032988569499497325534946263141290600932980283879589627719508486146330706341042145043308693086531962226954974409160193410486559975947551452252186070052076137502484546705969917686261501611487944711980198750335363868777255314978549287255288023040659789982757550885714699072498245794184
    g=2
    p=27341575807763915440957436428535182220000142184360678911922806134491171513601962928327153348379807003733212430441448335485539392927243408042052390132908460163622584761057456708037688348575981208568914166389954528379694087283746499739482793397547460009641464925892388008516688501843729426533031109155115312446405006471151097937294746430880161881055644049400477438004282947912557557327202968235636217357700570278135233543883386833783302503437400921214847918691618728831336071363513428886080975814569778943504942469750897997196854760936021938339670540667623962202131066843992659136047477962518548417233315488799010007419
    
    # equivalent of what asyncssh is doing
    root.info(f"Using cryptography {cryptography.__version__}")
    root.info("1")
    pn = dh.DHParameterNumbers(p, g)
    root.info("2")
    priv_key = pn.parameters().generate_private_key()
    root.info("3")
    pub_key = priv_key.public_key()
    root.info("4")
    pub_key.public_numbers().y
    root.info("5")
    peer_key = dh.DHPublicNumbers(peer_public, pn).public_key()
    root.info("6")
    shared_key = priv_key.exchange(peer_key)
    root.info("7")
    shared = int.from_bytes(shared_key, 'big')
    root.info("8")

main()
