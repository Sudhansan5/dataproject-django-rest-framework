/* 
    Create Database and Role
*/
CREATE ROLE sudhanshu_django CREATEDB LOGIN PASSWORD 'abc';

CREATE DATABASE sudhanshu_django WITH OWNER sudhanshu_django;
