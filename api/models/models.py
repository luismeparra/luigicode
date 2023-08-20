# models/models.py
###
import logging

# Configure logging for models module
log_format = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(filename='models.log', level=logging.DEBUG, format=log_format)

# 

from pydantic import BaseModel

#######

class PassengerSatisfaction(BaseModel):
    id: int
    Gender: str
    Customer_Type: str
    Age: float
    Type_of_Travel: str
    Class: str
    Flight_Distance: float
    Inflight_wifi_service: int
    Departure_Arrival_time_convenient: int
    Ease_of_Online_booking: int
    Gate_location: int
    Food_and_drink: int
    Online_boarding: int
    Seat_comfort: int
    Inflight_entertainment: int
    On_board_service: int
    Leg_room_service: int
    Baggage_handling: int
    Checkin_service: int
    Inflight_service: int
    Cleanliness: int
    Departure_Delay_in_Minutes: float
    Arrival_Delay_in_Minutes: float
    satisfaction: str
