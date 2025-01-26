import re 
from  collections import Counter

def main():

    try:
        error_count = 0
        error_timestamps = []
        ip_addresses = []
        
        error_pattern=re.compile(r"ERROR")
        timestamp_pattern =re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}") 
        ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
        
        with open("server.log","r") as r:
            for line in r:

                # get info if any error is occure in line
                if error_pattern.search(line):
                    error_count+=1
                    timestamp_match=timestamp_pattern.search(line)
                    
                    # extrect timestamp from line
                    if timestamp_match:
                        error_timestamps.append(timestamp_match.group())
                
                # extrect ip information
                ip_match=ip_pattern.search(line)
                if ip_match:
                    ip_addresses.append(ip_match.group())
        
        # Summarize results
        ip_counts = Counter(ip_addresses)  # Count occurrences of each IP
        print(f"Total errors found: {error_count}")
        print(f"Timestamps of errors: {error_timestamps}")
        print("Most common IP addresses:")
        for ip, count in ip_counts.most_common(5):
            print(f"{ip}: {count} occurrences")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
