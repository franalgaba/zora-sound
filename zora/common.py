from zora.queries import LIST_NFT_QUERY
from zora.utils import run_zora_query
from zora.nft import NFT


def list_nft():

    """

    List all NFT Collections tracked by ZORA

    Returns:
        List[NFT]: list of NFT Objects
    """

    data = run_zora_query(LIST_NFT_QUERY)
    result = []
    for contract in data["data"]["TokenContract"]:
        result.append(NFT(contract["address"]))
    return result
