import sys
import argparse
from fetch import fetch_package
from decrypt import decrypt_package
from install import install_package
from yank import yank_package
from utils import setup_logging, log, load_config, ensure_dir

def main():
    parser = argparse.ArgumentParser(description="murc - viaWX Package Manager")
    parser.add_argument('command', choices=['install', 'remove', 'update', 'yank', 'list', 'info'], help="Command to execute")
    parser.add_argument('package', nargs='?', help="Package name")
    parser.add_argument('--version', help="Specify package version")
    parser.add_argument('--debug', action='store_true', help="Enable debug mode")
    
    args = parser.parse_args()
    
    setup_logging(args.debug)
    config = load_config()
    ensure_dir(config["package_directory"])
    
    if args.command == 'install':
        if args.package:
            log("INFO", f"Installing package {args.package}")
            package_data = fetch_package(args.package, args.version)
            if package_data:
                decrypted_data = decrypt_package(package_data)
                if decrypted_data:
                    install_package(decrypted_data)
        else:
            log("ERROR", "Package name is required for install command")
            sys.exit(1)
    elif args.command == 'remove':
        # TODO
        pass
    elif args.command == 'update':
        # TODO
        pass
    elif args.command == 'yank':
        if args.package and args.version:
            log("INFO", f"Yanking package {args.package} to version {args.version}")
            yank_package(args.package, args.version)
        else:
            log("ERROR", "Package name and version are required for yank command")
            sys.exit(1)
    elif args.command == 'list':
        # TODO
        pass
    elif args.command == 'info':
        # TODO
        pass

if __name__ == "__main__":
    main()
