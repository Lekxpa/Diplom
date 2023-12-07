from telegram import Bot 
from dataclasses import dataclass


@dataclass
class Tok_adm:
    token: str = '6634382782:AAFkVB2hHVod7ABrAYTgDq5AKB5QNv50Co4'
    # admin: str =  '6551035386'
 
    
bot = Bot(token=Tok_adm.token)