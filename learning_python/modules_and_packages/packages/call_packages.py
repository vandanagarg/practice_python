from mypackage import main_program
from mypackage.sub_package import sub_program

main_program.mainprogram()

sub_program.subprogram()

## In order to manually edit/add the path in sys path
import sys
sys.path.append("D:\\git\\practice_python\\learning_python\\modules_and_packages\\packages\\mypackage")
print(sys.path)


