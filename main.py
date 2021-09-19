import system_health as sh

from rich import print,box
from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.console import Console

console = Console()

grid = Table.grid(expand=True)
grid.add_column(justify="center", ratio=1)
grid.add_column(justify="right")
grid.add_row(
    "System Health Tool",
    datetime.now().ctime().replace(":", "[blink]:[/]"),
)
print(Panel(grid, style="white on blue"))

def fn_menu():
    grid1 = Table(expand=True,border_style="white")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","Available RAM"
    )
    grid1.add_row(
        "2","Load Average"
    )
    grid1.add_row(
        "3","Hostname Details"
    )
    grid1.add_row(
        "4","All Process Count"
    )
    grid1.add_row(
        "5","Display uptime"
    )
    grid1.add_row(
        "7","Exit"
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")

def ram_rich():
    total,used,free = sh.free_ram()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Ram Deatails[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        f"Available RAM : {free}"
    )
    grid1.add_row(
        f"Used RAM : {used}"
    )
    grid1.add_row(
        f"Total RAM : {total}"
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    choice()

def load_rich():
    ld = sh.load_avg()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Load Average[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        ld
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    choice()

def host_rich():
    hst = sh.hostname()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Hostname Status[#FFF300]",justify="right",style="#FFF300")
    grid1.add_column(style="bright_green")
    grid1.add_row(
        "Static hostname : ",hst['Static hostname']
    )
    grid1.add_row(
        "Icon name : ", hst["Icon name"]
    )
    grid1.add_row(
        "Chassis : ",hst["Chassis"]
    )
    grid1.add_row(
        "Operating System : ",hst["Operating System"]
    )
    grid1.add_row(
        "Kernel : ",hst["Kernel"]
    )
    grid1.add_row(
        "Architecture : ",hst["Architecture"]
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    choice()

def pc_rich():
    cnt = sh.ps_count()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Process Count[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        cnt
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    choice()

def up_rich():
    up = sh.up_time()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Up Time[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        up
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    choice()


def choice():
    fn_menu()
    ch = int(input())
    if ch == 1:
        ram_rich()
    elif ch == 2:
        load_rich()
    elif ch == 3:
        host_rich()
    elif ch == 4:
        pc_rich()
    elif ch == 5:
        up_rich()
    elif ch == 7:
        exit()
    else:
        print("\n invalid choice")
        choice()

choice()