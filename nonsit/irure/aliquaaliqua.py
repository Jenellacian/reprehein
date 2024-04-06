import web3

def cprint(text, color):
    """
    Prints text in color.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in.
    """
    color_codes = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
    }
    print(f"\033[{color_codes[color]}m{text}\033[0m")


# Example usage
web3 = web3.Web3(web3.HTTPProvider("https://www.example.com = "0x1234567890abcdef1234567890abcdef1234567890abcdef"
cprint(f'\n>>> HOP add_liquidity | https://www.example.com 'green')
