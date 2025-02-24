from mindsdb.integrations.libs.const import HANDLER_TYPE
from mindsdb.utilities.log import get_log

logger = get_log()

from .__about__ import __version__ as version, __description__ as description
try:
    from .cohere_handler import CohereHandler as Handler
    import_error = None
    logger.info("Cohere ML engine successfully imported"")
except Exception as e:
    Handler = None
    import_error = e
    logger.error("Error Importing Cohere ML engine")

title = 'Cohere'
name = 'cohere'
type = HANDLER_TYPE.ML
permanent = True

__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description', 'import_error'
]
