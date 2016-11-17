
import random

# from http://stackoverflow.com/questions/3589214/generate-multiple-random-numbers-to-equal-a-value-in-python

# see also http://stackoverflow.com/questions/18659858/generating-a-list-of-random-numbers-summing-to-1
def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

number_of_sections=10
print(number_of_sections)

number_of_books=3 # must be less than number of sections
shuffled_indices=range(number_of_sections)
random.shuffle(shuffled_indices)
print("shuffled indices:")
print(shuffled_indices)

count_ary=constrained_sum_sample_pos(number_of_books, number_of_sections)
print("how to split the indices into books:")
print(count_ary)

assignment_dic={}
initial_index=0
for book_index,section_count in enumerate(count_ary):
#     print book_index,section_count
    
    final_index=initial_index+section_count
#     print(shuffled_indices[initial_index:final_index])

    assignment_dic["book "+str(book_index)]=shuffled_indices[initial_index:final_index]

    initial_index=final_index

print("resulting assignment:")
print(assignment_dic)


# begin random guesses

list_of_random_choices=[]
for this_section_indx in range(number_of_sections):
    for potential_similar_section_indx in range(this_section_indx+1,number_of_sections):
        for indx,existing_list in enumerate(list_of_random_choices):
            if (this_section_indx in existing_list) and (potential_similar_section_indx in existing_list):

        if (random.randint(0,1)==0):
            print("this sec: "+str(this_section_indx)+", pot sec: "+str(potential_similar_section_indx)+", matches")
            this_section_already_in_list=False
            for indx,existing_list in enumerate(list_of_random_choices):
                if (this_section_indx in existing_list):
                     list_of_random_choices[indx].append(potential_similar_section_indx)
                     this_section_already_in_list=True
            if (not this_section_already_in_list):      
                this_list=[this_section_indx,potential_similar_section_indx]
                list_of_random_choices.append(this_list)
        else:
            print("this sec: "+str(this_section_indx)+", pot sec: "+str(potential_similar_section_indx)+", does not match")

        print(list_of_random_choices)
        
        