#  Copyright © DataSpark Pte Ltd 2014 - 2020.
#
#  This software and any related documentation contain confidential and proprietary information of
#  DataSpark and its licensors (if any). Use of this software and any related documentation is
#  governed by the terms of your written agreement with DataSpark. You may not use, download or
#  install this software or any related documentation without obtaining an appropriate licence
#  agreement from DataSpark.
#
#  All rights reserved.

"""
   This is basic operations for configuration before starting query

   @author: jingxuan
   @maintainer: jingxuan
   @last editor: jingxuan
   @last edit time: 3/4/20
"""

from genomeapi.config import Config
from genomeapi.api import Authorize, DiscreteVisit, LinkMeta, ODMatrix, ODThroughLink, StayPoint

class Dspark:
  #_URL = "https://apistore.dsparkanalytics.com.au"

  def __init__(self,
               URL = "https://apistore.dsparkanalytics.com.au",
               token=None,
               site: str = "DEFAULT",
               ):
    if token is None:
      ## token not given, trying to fetch with given consumer_key and secret
      self.config = Config(site)

      self.auth = Authorize(url=URL+"/token",
                            consumer_key=self.config.consumer_key,
                            consumer_secret=self.config.consumer_secret)
      _token = self.auth._token
    else:
      ## token is given, use the token directly
      _token = token

    _URL = URL
    self.stay_point = StayPoint(_URL, _token)
    self.link_meta = LinkMeta(_URL, _token)
    self.discrete_visit = DiscreteVisit(_URL, _token)
    self.od_matrix = ODMatrix(_URL, _token)
    self.od_through_link = ODThroughLink(_URL, _token)
    self.URL = URL
