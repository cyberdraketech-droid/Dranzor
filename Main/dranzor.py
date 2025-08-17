import argparse
from modules import (
    file_reverse,
    website_reverse,
    binary_decompiler,
    obfuscation_analysis,
    pe_analyzer,
    disassembler,
    extractor,
    webanalyzer,
    apk_analyzer
)

def show_blue_dragon():
    blue = "\033[94m"
    reset = "\033[0m"
    print(blue + r"""
          
                                       
                        ___====-_  _-====___
                  _--^^^#####//      \\#####^^^--_
               _-^##########// (    ) \\##########^-_
              -############//  |\^^/|  \\############-
            _/############//   (O::O)   \\############\_
           /#############((     \\//     ))#############\
          -###############\\    (oo)    //###############-
         -#################\\  / `' \  //#################-
        -###################\\/  (_)  \//###################-
       _#/|##########/\######(   '/'   )######/\##########|\#_
           
        ██████╗ ██████╗ █████╗  ███╗   ██╗███████╗███████╗█████╗
        ██╔══██╗██╔══██╗██╔══██╗████╗  ██║╚══███╔╝██╔════╝██╔══██╗
        ██║  ██║██████╔╝███████║██╔██╗ ██║ ███╔╝  █████╗  ██████╔╝
        ██║  ██║██║  ██║██╔══██║██║╚██╗██║ ███╔╝  ██╔══╝  ██║  ██
        ██████╔╝██║  ██║██║  ██║██║ ╚████║███████╗███████╗██║  ██
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╚═╝  ╚═╝


                 The Ultimate Reverse Engineering Tool
    """ + reset)

def main():
    show_blue_dragon()
    parser = argparse.ArgumentParser(description="Dranzer- Reverse Engineering Toolkit")
    parser.add_argument("-f", "--file", help="Reverse engineer a file", metavar="FILE")
    parser.add_argument("-w", "--website", help="Reverse engineer a website", metavar="URL")
    parser.add_argument("-d", "--decompile", help="Decompile binary file", metavar="BINARY")
    parser.add_argument("-o", "--obfuscation", help="Analyze obfuscation of code file", metavar="CODE")
    parser.add_argument("-p", "--pe", help="Analyze PE file", metavar="PEFILE")
    parser.add_argument("-ds", "--disassemble", help="Disassemble binary file", metavar="BINARY")
    parser.add_argument("-e", "--extract", help="Extract embedded resources from file", metavar="FILE")
    parser.add_argument("-wa", "--webanalyze", help="Analyze website deeply", metavar="URL")
    parser.add_argument('--apk', help="Analyze APK file")

    args = parser.parse_args()
    if args.apk:
        apk_analyzer.analyze_apk(args.apk)
    if args.file:
        file_reverse.reverse_file(args.file)
    if args.website:
        website_reverse.reverse_website(args.website)
    if args.decompile:
        binary_decompiler.disassemble_binary(args.decompile)
    if args.obfuscation:
        obfuscation_analysis.analyze_obfuscation(args.obfuscation)
    if args.pe:
        pe_analyzer.analyze_pe(args.pe)
    if args.disassemble:
        disassembler.disassemble_binary(args.disassemble)
    if args.extract:
        extractor.extract_resources(args.extract)
    if args.webanalyze:
        webanalyzer.analyze_website(args.webanalyze)
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
