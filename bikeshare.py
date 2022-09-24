import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s input for city (chicago, new york city, washington)!')
    flag = False
    while(not flag):
        city = input().lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            flag = True
        else:
            flag = False
            print("Your input is not valid!")
            print('Let\'s input for city again (chicago, new york city, washington)!')

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Hello! Let\'s input for month (all, january, february, ... , june)!')
    flag = False
    while(not flag):
        month = input().lower()
        if month == 'all':
            flag = True
        elif month == 'january':
            flag = True
        elif month == 'february':
            flag = True
        elif month == 'march':
            flag = True
        elif month == 'april':
            flag = True
        elif month == 'may':
            flag = True
        elif month == 'june':
            flag = True
        elif month == 'july':
            flag = True
        elif month == 'august':
            flag = True
        elif month == 'september':
            flag = True
        elif month == 'october':
            flag = True
        elif month == 'november':
            flag = True
        elif month == 'december':
            flag = True
        else:
            flag = False
            print("Your input is not valid!")
            print('Let\'s input for month again (all, january, february, ... , june)!')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Hello! Let\'s input day of week (all, monday, tuesday, ... sunday)!')
    flag = False
    while(not flag):
        day = input().lower()
        if day == 'all':
            flag = True
        elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
            flag = True
        else:
            flag = False
            print("Your input is not valid!")
            print('Let\'s input day of week again (all, monday, tuesday, ... sunday)!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # filter by city
    for p,v in CITY_DATA.items():
        if city == p:
            print(v)
            df = pd.read_csv(v)         
    
    # convert the Start Time column to datetime
    try:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # extract month and day of week from Start Time to create new columns
        df['Month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour
    
        # filter by month
        if month != 'all':
            # use the index of the months list to get the corresponding int
            month = months.index(month) + 1
            # filter by month to create the new dataframe
            df = df[df['Month'] == month]
        
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
    except:
        print('\nThis city does not have Start Time data')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    cmMonth = str(months[df['Month'].mode()[0]-1])
    print('The most common month is ' + cmMonth.capitalize())

    # TO DO: display the most common day of week
    print('\nThe most common day of week is ' + str(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        print('The most commonly used start station is ' + str(df['Start Station'].mode()[0]))
    except:
        print('\nThis city does not have Start Station data')

    # TO DO: display most commonly used end station
    try:
        print('The most commonly used end station is ' + str(df['End Station'].mode()[0]))
    except:
        print('\nThis city does not have End Station data')

    # TO DO: display most frequent combination of start station and end station trip
    df['Combi Station'] = df['Start Station'] + df['End Station']
    print('The most frequent combination of start station and end station trip is ' + str(df['Combi Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # logic of calculate total travel time and mean travel time
    count = len(df.index)
    try:
        totalTime = df['Trip Duration'].sum()
        avgTime = int(totalTime/count/60)
    except:
        try:
            df['Start Time'] = pd.to_datetime(df['Start Time'])
        except:
           print('\nThis city does not have Start Time data')
        try:
            df['End Time'] = pd.to_datetime(df['End Time'])
        except:
            print('\nThis city does not have End Time data')
        df['Travel_time'] = df['End Time'] - df['Start Time']
        totalTime = df["Travel_time"].sum()
        avgTime = int(totalTime/count/1e9/60)
        
    # TO DO: display total travel time
    print('Total travel time: ' + str(totalTime))
    
    # TO DO: display mean travel time
    print('\nMean travel time: ' + str(avgTime) + ' minutes')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: ')
    try:
        user_type_counts = df['User Type'].value_counts()
        print(user_type_counts)
    except:
        print('\nThis city does not have User Type data')

    # TO DO: Display counts of gender
    print('\nCounts of gender: ')
    try:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    except:
        print('\nThis city does not have Gender data')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nEarliest year of birth: ' + str(df['Birth Year'].min()))
        print('\nMost recent year of birth: ' + str(df['Birth Year'].max()))
        print('\nMost common year of birth: ' + str(df['Birth Year'].mode()[0]))
    except:
        print('\nThis city does not have Birth Year data')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    flag = True
    while(flag):
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
        if(view_data == 'yes'):
            start_loc = 0
            view_display = 'yes'
            flag = False
            while(True):
                if(view_display== 'yes'):
                    print(df.iloc[start_loc:start_loc+5, [4,5,3,6,7,8]])
                    start_loc += 5
                    view_display = input("Do you wish to continue? Enter yes or no? ").lower()
                elif(view_display == 'no'):
                    break
                else:
                    view_display = input("You input wrong data! Do you wish to continue? Enter yes or no? ").lower()
        elif(view_data == 'no'):
            flag = False
        else:
            print('You input wrong data')
            flag = True
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
