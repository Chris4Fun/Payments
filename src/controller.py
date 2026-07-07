from credentials import generate_creds
from list_mails import list_mails

def run_pipeline():
  print("Fetching credentials...")
  creds = generate_creds()

  print("Fetching 100 messages")
  list_mails(creds)


if __name__ == "__main__":
  run_pipeline()