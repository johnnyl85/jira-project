import jira
import getpass

def ticketResults(user, pw, jqlQuery):
	mecha = jira.JIRA('https://mechabugs.indeed.com', basic_auth=(user, pw))
	tickets = mecha.search_issues(jqlQuery)
	return tickets

def main():
	user = raw_input('username:')
	pw = getpass.getpass('password:')
	jqlQuery = 'project = AFM AND status = "Pending Technical Input" AND assignee in (membersOf(external-aggmaint-avantica)) AND (labels not in (low_quality_opa) OR labels is EMPTY) AND "Priority Issue" is EMPTY AND "Business Status" != Sponsored ORDER BY created ASC'
	ticketList = ticketResults(user, pw, jqlQuery)
	print ticketList

if __name__ == "__main__":
	main()
