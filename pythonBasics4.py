# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    counter = 0
    for i in emails:
            contacts[list(contacts.keys())[counter]] = i
            counter = counter + 1
    return contacts


# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    if len(contact_info)<1:
        return contacts
    if len(contact_info[0])<1:
        return contacts

    x = 0
    for i in contacts:
        contacts[i] = {"email": contact_info[x][0], "phone": contact_info[x][1]}
        x += 1
    return contacts

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE
    #store every 1,2,3 values in arr
    #store arrs in big arr
    #return big arr

    names = []
    emails = []
    phones = []
    bigArr = [emails,phones,names]

    for key, value in contacts.items():
        names.append(key)
        emails.append(value)
        #print(emails)
    #for i in contacts:
            #contacts[list(contacts.keys())[counter]] = i
            #counter = counter + 1
    return bigArr

