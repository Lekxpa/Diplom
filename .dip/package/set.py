from telegram import Bot 
from dataclasses import dataclass


@dataclass
class Top:
    token: str = '6634382782:AAFkVB2hHVod7ABrAYTgDq5AKB5QNv50Co4'
    admin: int =  5199358937
    
    
bot = Bot(token=Top.token)