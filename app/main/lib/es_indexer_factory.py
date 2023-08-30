from app.main.lib.es_indexer_test import ESIndexerTest


class ESIndexerFactory(object):
    """
    ES Factory class
    """

    @staticmethod
    def create_indexer(index_name):
        match index_name:
            case 'unit_test':
                return ESIndexerTest(index_name)
            case _:
                return
