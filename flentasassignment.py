def check_permutation_exists(text, scribbled_text):
    scribbled_freq = [0] * 256
    window_freq = [0] * 256
    n = len(scribbled_text)
    m = len(text)

    # Count frequency of each character in scribbled_text
    for i in range(n):
        scribbled_freq[ord(scribbled_text[i])] += 1

    # Initialize window
    for i in range(n):
        window_freq[ord(text[i])] += 1

    # Check if window is a permutation of scribbled_text
    if window_freq == scribbled_freq:
        return True

    # Slide window over text
    for i in range(n, m):
        window_freq[ord(text[i])] += 1
        window_freq[ord(text[i-n])] -= 1

        # Check if window is a permutation of scribbled_text
        if window_freq == scribbled_freq:
            return True

    return False


# Read number of test cases
T = int(input())

for i in range(T):
    # Read pattern and text strings
    scribbled_text = input().strip()
    text = input().strip()

    # Check if permutation of scribbled_text exists in text
    if check_permutation_exists(text, scribbled_text):
        print("YES")
    else:
        print("NO")
