import socket

def dns_lookup(query):
    """
    Performs a DNS lookup for a given hostname or IP address.
    If a hostname is provided, it returns the corresponding IP address.
    If an IP address is provided, it attempts to return the corresponding hostname.
    """
    try:
        # Attempt to resolve as a hostname to get an IP address
        ip_address = socket.gethostbyname(query)
        print(f"Hostname: {query} -> IP Address: {ip_address}")

        # Attempt a reverse lookup if the query was initially an IP
        if query == ip_address: # This indicates the query was likely an IP address
            try:
                # gethostbyaddr returns (hostname, aliaslist, ipaddrlist)
                # We use _, _ to ignore the aliaslist and ipaddrlist
                hostname, _, _ = socket.gethostbyaddr(ip_address)
                print(f"IP Address: {ip_address} -> Hostname: {hostname}")
            except socket.herror:
                 print(f"Could not resolve hostname for IP address: {ip_address}")
        else:
            pass # The query was a hostname, so we already have the IP

    except socket.gaierror:
        # If gethostbyname fails, it might be an invalid hostname or an IP
        try:
            # Attempt to resolve as an IP address to get a hostname (reverse DNS)
            hostname, _, _ = socket.gethostbyaddr(query)
            print(f"IP Address: {query} -> Hostname: {hostname}")
        except socket.herror:
            print(f"Could not resolve '{query}'. Please check the input.")
        except socket.gaierror:
            print(f"Invalid input: '{query}'. Please enter a valid hostname or IP address.")

def main():
    while True:
        user_input = input("Enter a hostname or IP address (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        if user_input:
            dns_lookup(user_input)
        else:
            print("Input cannot be empty.")

# Corrected from the PDF's "if_name__"
if __name__ == "__main__":
    main()