import sunny_status
import kel_status

#sunny_statusとkel_statusを__all__に登録する -> import * で読み込むとき、__all__に記述したモジュールがimportされる(非推奨)

__all__ = ['sunny_status', 'kel_status']

print("__init__が読み込まれました")
print(__all__)