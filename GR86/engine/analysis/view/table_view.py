from tabulate import tabulate
import webbrowser
import os


def get_tabulate_view(table, file_name):
    """

    :param table:
    :param file_name:
    :return:
    """
    html = f"""\
        <title>{file_name}</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style type="text/css">
            table
            {{
                border-collapse: collapse;
                margin: 0 auto;
                text-align: center;
            }}
            table td, table th
            {{
                border: 1px solid #cad9ea;
                color: #666;
                height: 50px;
                min-width: 200
            }}
            table thead th
            {{
                background-color: #CCE8EB;
                width: 180px;
            }}
            table tr:hover 
            {{
                background: #F5FAFA;
    
            }}
    
        </style>
    </head> 
    <body> 
    {tabulate(table, headers='keys', tablefmt="html")}
    </body>
    
    </html>
    """
    filename = f"${file_name}.html"
    with open(filename, 'w') as f:
        f.write(html)
        f.close()
    webbrowser.open('file://' + os.path.realpath(filename))

