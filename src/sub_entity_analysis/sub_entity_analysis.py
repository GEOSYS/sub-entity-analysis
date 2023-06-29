import numpy as np
from geosyspy.geosys import Geosys
from geosyspy.utils import constants



class SubEntityAnalysis():
    """SubEntityAnalysis is the class to generate 2 times series on a specific indicator and compare them between each others

    Parameters:
        client_id (str): The client id
        client_secret (str): The client secret
        username (str): The api username
        password (str): The api user password
        enum_env (enum): 'Env.PROD' or 'Env.PREPROD'
        enum_region (enum): 'Region.NA' or 'Region.EU'
        priority_queue (str): 'realtime' or 'bulk'
    """
    def __init__(self, client_id: str,
                 client_secret: str,
                 username: str,
                 password: str,
                 enum_env: enumerate,
                 enum_region: enumerate,
                 priority_queue: str = "realtime",
                 ):

        self.region: str = enum_region.value
        self.env: str = enum_env.value
        self.priority_queue: str = priority_queue
        self.__client: Geosys = Geosys(client_id, client_secret, username, password, enum_env, enum_region, priority_queue)


    def get_satellite_image_time_series_indicator(self, polygon, start_date, end_date, indicator):
        """Retrieve a pixel-by-pxel time series of the indicator on the MR collections targeted by using geosyspy library

                Args:
                    polygon (str): The polygon
                    start_date (datetime): The start date of the time series
                    end_date (datetime): The end date of the time series
                    indicator (str): Indicators to retrieve on the collections

                Returns:
                    (xarray dataset): xarray dataset for the time series
                """
        return self.__client.get_satellite_image_time_series(polygon,
                                                             start_date,
                                                             end_date,
                                                             collections=[constants.SatelliteImageryCollection.SENTINEL_2, constants.SatelliteImageryCollection.LANDSAT_8,
                                                                          constants.SatelliteImageryCollection.LANDSAT_9],
                                                             indicators=[indicator])

    def get_cumulative_index_calculation(self, data_set, indicator):
        """ get the cumulative value of the indicator over time

                Args:
                    data_set (Xarray dataset): The xarray dataset built on one indicator for a polygon
                    indicator (str): the indicator value used to create the data_set

                Returns:
                    cumul_index_ds (xarray dataarray) : xarray dataarray representing the cumulative value of the indicator over time
        """
        # indicator band result from data_set, sort by time
        indicator_ds = data_set[indicator].sortby('time')

        # exclude Nan values to caluculate mean
        masked_data_array = indicator_ds.where(~np.isnan(indicator_ds))

        # index mean calculation
        mean_index = masked_data_array.mean(dim=['x', 'y'])

        # Cumulative Index calculation
        cumul_index_ds = mean_index.cumsum(dim='time')

        return cumul_index_ds

    def get_deviation_percentage (self, polygon_cumul_index_da, sub_polygon_cumul_index_da):
        """ get the deviation percentage between 2 xarray dataarray

                Args:
                    polygon_cumul_index_da (Xarray dataarray): The xarray dataarray of the main polygon
                    sub_polygon_cumul_index_da (Xarray dataarray): The xarray dataarray of the sub polygon

                Returns:
                    deviation_percentage (xarray dataarray) : xarray dataarray representing the cumulative value of the indicator over time
                """
        deviation_percentage = ((polygon_cumul_index_da - sub_polygon_cumul_index_da) / polygon_cumul_index_da) * 100

        return deviation_percentage