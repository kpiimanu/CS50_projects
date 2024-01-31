-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Pulling info from crime_scene_reports table using the date and location of the t
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND year = 2021
AND street = 'Humphrey Street';

-- New lead: took place at 10:15am at the Humphrey Street bakery & 3 witnesses.
-- Will look into bakery_security_logs
SELECT activity, hour, minute FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2021
AND hour = 10 AND minute BETWEEN 12 AND 20;
-- no lead

-- Will look into interviews
SELECT id, transcript FROM interviews
WHERE month = 7 AND day = 28 AND year = 2021
AND trancript LIKE "%bakery%";

-- 161. transcripts: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- 162. I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- 163. As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that THEY were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- New lead: checking bakery_security_logs since there was a car parked that thief left in.
--According to witness, they left within 10 min of theft. will use the 10 min window in code.
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE month = 7 AND day = 28 AND year = 2021
AND hour = 10 AND minute >= 15 AND minute <= 25
AND activity = 'exit';

-- List of names resulted for suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, & Kelsey

-- Next lead: look into thief withdrawing money from ATM on Leggett Street
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE month = 7 AND day = 28 AND year = 2021
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- New suspect list: Bruce, Luca, Iman, & Diana (other names were omitted since they were not in previous list)

-- Next lead: thief took first flight out the next day. WIll check first flight out 7/29/2021
--first to get airport ID and use with data in flights
SELECT id, full_name FROM airports
WHERE city = 'Fiftyville';

--name of airport = Fiftyville Regional Airport & ID = 8

-- Use ID of airport to investigate flights
SELECT destination_airport_id FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE month = 7 AND day = 29 AND year = 2021
ORDER BY hour, minute
LIMIT 1;

-- Destination airport id = 4... flight went from id 8 to 4. LaGuardia Airport
-- look into destination airport name
SELECT full_name, city FROM airports
WHERE id = 4;

-- *** destination was New York City that theif & accomplice fled to

-- Circle back to flight and use origin aiport (8) & destination airport (6) info to locate flight id
SELECT id FROM flights
WHERE origin_airport_id = 8 AND destination_airport_id = 4
AND month = 7 AND day = 29 AND year = 2021
ORDER BY hour AND minute ASC;

-- flight id = 36. use in conjuction with passengers
SELECT passport_number FROM passengers
WHERE flight_id = 36;

-- passport numbers of people on flight =  7214083635, 1695452385,
--  5773159633, 1540955065, 8294398571, 1988161715, 9878712108,8496433585

-- There was probably an easier way to do this but I used this same code over and over with the passport numbers to get the list of names of the passengers.
SELECT name FROM people
WHERE passport_number = 7214083635;
-- DORIS

SELECT name FROM people
WHERE passport_number = 1695452385;
--SOFIA

SELECT name FROM people
WHERE passport_number = 5773159633;
-- BRUCE*

SELECT name FROM people
WHERE passport_number = 1540955065;
-- EDWARD

SELECT name FROM people
WHERE passport_number = 8294398571;
--KELSEY

SELECT name FROM people
WHERE passport_number = 1988161715;
-- TAYLOR

SELECT name FROM people
WHERE passport_number = 9878712108;
-- KENNY

SELECT name FROM people
WHERE passport_number = 8496433585;
-- LUCA*

-- Bruce & Luca are the only common suspects
-- Go into phone call that occured for less than a minute

SELECT name FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE month = 7 AND day = 28 AND year = 2021
AND duration < 60;
-- THIEF IDENTIFIED: BRUCE

-- need Bruce's phone number
SELECT phone_number FROM people
WHERE name = 'Bruce' AND passport_number = 5773159633;

-- Bruce's phone number is (367) 555-5533

-- Now to get phone number of accomplice using receiver
SELECT receiver FROM phone_calls
WHERE caller = '(367) 555-5533'
AND month = 7 AND day = 28 AND year = 2021
AND duration < 60;

-- receiver phone number is (375) 555-8161
-- now to id accomplice
SELECT name FROM people
WHERE phone_number = '(375) 555-8161';

-- *** ACCOMPLICE IS ROBIN!!