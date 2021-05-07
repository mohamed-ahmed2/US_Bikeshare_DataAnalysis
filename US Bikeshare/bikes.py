import time
import pandas as pd
import numpy as np
from datetime import datetime as dt
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago' , 'new york' , 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday','wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
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
    city = input('would you like to see data for chicago , new york or washington\n')
    while city.lower() not in cities :
        print('this is not a valid city name')
        city = input('would you like to see data for chicago , new york or washington\n')
        if city.lower() in cities :
            print(f'looks like you want to hear about {city} ! if this is not true , restart the program now')
            break
    decision = input('would you like to filter data by month , day , or not at all ? type none for no time filter\n')
    if decision.lower() != 'month' and decision.lower() != 'day':
        month = None
        day = None

    elif decision.lower() == 'month':
        day = None
        print('we will make sure to filter by  month')
        month = input('which month ? january , febraury , march , april , may or june ? please type out the full month name : \n')
        while month.lower() not in months:
            print('this is not  a valid month name')
            month = input('which month ? january , febraury , march , april , may or june ? please type out the full month name : \n')

    elif decision.lower() == 'day':
        month = None
        print('we will make sure to filter by  day')
        day = input('which day ? monday , tuesday , wednesday , thursday , friday , saturday or sunday ? please type out the full day name : \n')

        while day.lower() not in days:
            print('this is not  a valid day name')
            day = input('which day ? monday , tuesday , wednesday , thursday , friday , saturday or sunday ? please type out the full day name : \n')


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != None :
        if month != 'all' and month.lower() in months:
            # use the index of the months list to get the corresponding int

            month = months.index(month.lower()) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != None :
        if day != 'all' and day.lower() in days:
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #me converting start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print(f'the most common month is {most_common_month}')
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    most_common_day_of_the_week = df['day_of_week'].mode()[0]
    print(f'the most common day of the week is {most_common_day_of_the_week}')
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    #values = df['hour'].value_counts()

    popular_hour = df['hour'].mode()[0]
    print(f'the most common start hour is {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'the most common start station is {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'the most common End station is {popular_end_station}')

   # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'most frequent combination of start station and end station trip is {combination}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #df['Duration'] = pd.to_timedelta(df['Duration'])

    total_travel_time = df['Trip Duration'].sum()
    print(f'the total travel time is {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'the mean travel time is {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df :
        gender = df['Gender'].value_counts()
        print(gender)

    if 'Birth Year' in df:
        df['year'] = df['Birth Year']
        # TO DO: Display earliest, most recent, and most common year of birth
        earlist = df['year'].min()
        print(f'the earliest year is {earlist}')
        most_recent = df['year'].max()
        print(f'the most recent year is {most_recent}')

        most_common_year = df['year'].mode()[0]
        print(f'the most common year is {most_common_year}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """
    Displays raw data  upon request of the user.
    Args:

    (str) city - name of the city to analyze

    """

    display_raw = input('would you like to view individual trip data? Type yes or no\n')

    while display_raw == 'yes':
        for chunck in pd.read_csv(CITY_DATA[city.lower()] , chunksize=5) :
            print(chunck)
            display_raw = input('May you want to have a look on more raw data? Type yes or no\n')

            if display_raw.lower() != 'yes':
                    break

                # repeating the question

    if display_raw != 'yes':
        print('Thank You')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        #display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        if restart.lower() == 'yes':
            continue


if __name__ == "__main__":
	main()
