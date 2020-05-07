"Tiene Author-Gender-Editorial"
from .model_KindOfDescription import Author
from .model_KindOfDescription import Gender
from .model_KindOfDescription import Editorial

"tiene creditCards"
from .model_CreditCards import CreditCards

"tiene la generación de tablas para confirmar mail y cambio de mail"
from .model_MailToConfirm import  MailToConfirm

"tiene Account"
from .model_Account import Account

"tiene publication-book-bookbychapter-billboard-chapter"
from .model_Publication import Publication
from .model_Publication import Book
from .model_Publication import BookByChapter
from .model_Publication import Chapter
from .model_Publication import Billboard


"Tiene profile"
from .model_Profile import Profile

"Tiene Solicitudes de usuarios"
from .model_UserSolicitud import UserSolicitud

"Tiene Stados del libro en un perfil de usuario"
from .model_State_Of_Book import StateOfBook

"tiene like de publicacion y de comment"
from .model_Likes import Like
from .model_Likes import LikeComment

"tiene comment"
from .model_Comment import Comment

"tiene en que fecha se sube o se baja una publicación para premium y normal"
from .model_UpAndExpirationDates import UpDates
from .model_UpAndExpirationDates import ExpirationDates

"Tiene la cuenta de los estados del libro entre x fechas de inicio y fin"
from .model_CounterStates import CounterStates