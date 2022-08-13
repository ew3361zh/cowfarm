from view import *

from db.farm_database import SQLFarmDB

from view.view import View
from view_model import ViewModel

"""High level setup and starting view and database"""

def main():

    farm_db = SQLFarmDB()

    farm_view_model = ViewModel(farm_db)

    farm_view = View(farm_view_model)

    farm_view.get_new_pens()

    farm_view.run_time_series()

    farm_view.calculate_cost_and_ghg()    


if __name__ == '__main__':
    main()

