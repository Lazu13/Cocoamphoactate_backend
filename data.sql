DELETE FROM auth_user;
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(1, 'testuser1', 'testpass1', 1, '2017-01-10 19:16:14.049388', 'test', 'test', 'user1@user.com', 1, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(2, 'testuser2', 'testpass2', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user2@user.com', 0, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(3, 'testuser3', 'testpass3', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user3@user.com', 0, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(4, 'testuser4', 'testpass4', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user4@user.com', 0, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(5, 'testuser5', 'testpass5', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user5@user.com', 0, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(6, 'testuser6', 'testpass6', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user6@user.com', 0, 1, '2017-01-10 19:06:14.049388');
INSERT INTO auth_user(id, username, password, is_superuser, last_login, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(7, 'testuser7', 'testpass7', 0, '2017-01-10 19:16:14.049388', 'test', 'test', 'user7@user.com', 0, 1, '2017-01-10 19:06:14.049388');

;


DELETE FROM authtoken_token;
INSERT INTO authtoken_token VALUES('testToken1', '2017-01-10 19:06:14.049388', 1);
INSERT INTO authtoken_token VALUES('testToken2', '2017-01-10 19:06:14.049388', 2);
INSERT INTO authtoken_token VALUES('testToken3', '2017-01-10 19:06:14.049388', 3);
INSERT INTO authtoken_token VALUES('testToken4', '2017-01-10 19:06:14.049388', 4);
INSERT INTO authtoken_token VALUES('testToken5', '2017-01-10 19:06:14.049388', 5);
INSERT INTO authtoken_token VALUES('testToken6', '2017-01-10 19:06:14.049388', 6);
INSERT INTO authtoken_token VALUES('testToken7', '2017-01-10 19:06:14.049388', 7);

DELETE FROM Cocoamphoactate_game;
INSERT INTO Cocoamphoactate_game VALUES(1, 'The Wither 3: Wild Hunt', 'PC/PS4/XBO', 'Wither is a wandering monster slayer made by CDProject RED.');
INSERT INTO Cocoamphoactate_game VALUES(2, 'The Elder Scrolls V: Skyrim', 'PC', 'Fifth game of The Elder Scrolls series made by Bethesda.');
INSERT INTO Cocoamphoactate_game VALUES(3, 'Assassins Creed: Unity', 'PC', 'Fifth game of Assassins Creed Series made by Ubisoft.');
INSERT INTO Cocoamphoactate_game VALUES(4, 'Rise of the Tomb Raider', 'PC', 'Successor of Tomb Raider from 2013 made by Crystal Dynamics.');
INSERT INTO Cocoamphoactate_game VALUES(5, 'Gothic', 'PC', 'First game of the iconic game Series made by Piranha Bytes.');

DELETE FROM Cocoamphoactate_favorites;
INSERT INTO Cocoamphoactate_favorites VALUES(1, 1, 5);
INSERT INTO Cocoamphoactate_favorites VALUES(2, 1, 1);
INSERT INTO Cocoamphoactate_favorites VALUES(3, 2, 2);
INSERT INTO Cocoamphoactate_favorites VALUES(4, 2, 3);
INSERT INTO Cocoamphoactate_favorites VALUES(5, 3, 5);
INSERT INTO Cocoamphoactate_favorites VALUES(6, 3, 4);
INSERT INTO Cocoamphoactate_favorites VALUES(7, 3, 1);
INSERT INTO Cocoamphoactate_favorites VALUES(8, 4, 5);
INSERT INTO Cocoamphoactate_favorites VALUES(9, 5, 2);
INSERT INTO Cocoamphoactate_favorites VALUES(10, 5, 4);
INSERT INTO Cocoamphoactate_favorites VALUES(11, 5, 5);
INSERT INTO Cocoamphoactate_favorites VALUES(12, 6, 1);
INSERT INTO Cocoamphoactate_favorites VALUES(13, 6, 2);
INSERT INTO Cocoamphoactate_favorites VALUES(14, 7, 1);
INSERT INTO Cocoamphoactate_favorites VALUES(15, 7, 5);

DELETE FROM Cocoamphoactate_friends;
INSERT INTO Cocoamphoactate_friends VALUES(1, 1, 2);
INSERT INTO Cocoamphoactate_friends VALUES(2, 1, 3);
INSERT INTO Cocoamphoactate_friends VALUES(3, 1, 4);
INSERT INTO Cocoamphoactate_friends VALUES(7, 6, 7);
INSERT INTO Cocoamphoactate_friends VALUES(8, 4, 6);
INSERT INTO Cocoamphoactate_friends VALUES(9, 5, 3);
INSERT INTO Cocoamphoactate_friends VALUES(10, 5, 7);

DELETE FROM Cocoamphoactate_friendspending;
INSERT INTO Cocoamphoactate_friendspending VALUES(4, 2, 4);
INSERT INTO Cocoamphoactate_friendspending VALUES(5, 2, 5);
INSERT INTO Cocoamphoactate_friendspending VALUES(6, 3, 6);

DELETE FROM Cocoamphoactate_gamelib;
INSERT INTO Cocoamphoactate_gamelib VALUES(1, 1, 1);
INSERT INTO Cocoamphoactate_gamelib VALUES(2, 1, 5);
INSERT INTO Cocoamphoactate_gamelib VALUES(3, 2, 1);
INSERT INTO Cocoamphoactate_gamelib VALUES(4, 2, 3);
INSERT INTO Cocoamphoactate_gamelib VALUES(5, 2, 4);
INSERT INTO Cocoamphoactate_gamelib VALUES(6, 3, 2);
INSERT INTO Cocoamphoactate_gamelib VALUES(7, 4, 1);
INSERT INTO Cocoamphoactate_gamelib VALUES(8, 4, 2);
INSERT INTO Cocoamphoactate_gamelib VALUES(9, 5, 5);
INSERT INTO Cocoamphoactate_gamelib VALUES(10, 6, 4);
INSERT INTO Cocoamphoactate_gamelib VALUES(11, 6, 3);
INSERT INTO Cocoamphoactate_gamelib VALUES(12, 7, 2);

DELETE FROM Cocoamphoactate_reviews;
INSERT INTO Cocoamphoactate_reviews VALUES(1, 1, 1, "great game");
INSERT INTO Cocoamphoactate_reviews VALUES(2, 1, 3, "awesome game");
INSERT INTO Cocoamphoactate_reviews VALUES(3, 1, 4, "best game I've played");
INSERT INTO Cocoamphoactate_reviews VALUES(4, 2, 2, "preety good game");
INSERT INTO Cocoamphoactate_reviews VALUES(5, 2, 6, "average game");
INSERT INTO Cocoamphoactate_reviews VALUES(6, 3, 4, "could be better");
INSERT INTO Cocoamphoactate_reviews VALUES(7, 4, 3, "test game");
INSERT INTO Cocoamphoactate_reviews VALUES(8, 4, 5, "test game");
INSERT INTO Cocoamphoactate_reviews VALUES(9, 5, 2, "test game");
INSERT INTO Cocoamphoactate_reviews VALUES(10, 5, 1, "awesome game");
INSERT INTO Cocoamphoactate_reviews VALUES(11, 5, 7, "best game");

DELETE FROM Cocoamphoactate_score;
INSERT INTO Cocoamphoactate_score VALUES(1, 1, 1, 5);
INSERT INTO Cocoamphoactate_score VALUES(2, 1, 3, 5);
INSERT INTO Cocoamphoactate_score VALUES(3, 1, 4, 5);
INSERT INTO Cocoamphoactate_score VALUES(4, 2, 2, 4);
INSERT INTO Cocoamphoactate_score VALUES(5, 2, 6, 3);
INSERT INTO Cocoamphoactate_score VALUES(6, 3, 4, 4);
INSERT INTO Cocoamphoactate_score VALUES(7, 4, 3, 5);
INSERT INTO Cocoamphoactate_score VALUES(8, 4, 5, 4);
INSERT INTO Cocoamphoactate_score VALUES(9, 5, 2, 4);
INSERT INTO Cocoamphoactate_score VALUES(10, 5, 1, 4);
INSERT INTO Cocoamphoactate_score VALUES(11, 5, 7, 5);
