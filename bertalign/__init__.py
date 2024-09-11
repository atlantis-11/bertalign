"""
Bertalign initialization
"""

__author__ = "Jason (bfsujason@163.com)"
__version__ = "1.1.0"

from bertalign.aligner import Bertalign
from bertalign.encoder import Encoder

def load_model(model_name="LaBSE"):
    return Encoder(model_name)

# See other cross-lingual embedding models at
# https://www.sbert.net/docs/pretrained_models.html
