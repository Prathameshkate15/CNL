import ipaddress

def get_subnet_info(ip_cidr):
    """
    Calculates and displays subnet information for a given IP address in CIDR notation.

    Args:
    ip_cidr (str): The IP address and CIDR prefix (e.g., "192.168.1.0/24").
    """
    try:
        # strict=False allows host bits to be set (e.g., 192.168.1.50/24)
        network = ipaddress.ip_network(ip_cidr, strict=False) 
        
        print(f"IP Network: {network}")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Netmask: {network.netmask}")
        
        # Check if it's a /31 or /32, which have different host rules
        if network.prefixlen >= 31:
             print("Number of Hosts: 0 (special case network)")
        else:
            # Subtract 2 for the network and broadcast addresses
            print(f"Number of Hosts: {network.num_addresses - 2}")
            print(f"First Usable Host: {network.network_address + 1}")
            print(f"Last Usable Host: {network.broadcast_address - 1}")

    except ValueError as e:
        print(f"Error: Invalid IP address or CIDR notation. {e}")

if __name__ == "__main__":
    while True:
        user_input = input("Enter IP address with CIDR (e.g., 192.168.1.0/24) or 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            break
            
        get_subnet_info(user_input)
        print("-" * 30)
