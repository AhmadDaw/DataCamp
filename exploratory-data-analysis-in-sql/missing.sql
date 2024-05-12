-- find number of missing values in ticker column
SELECT count(*) - count(ticker) AS missing
  FROM fortune500;

-- find number of missing values in industry column
SELECT count(*) - count(industry) AS missing
  FROM fortune500;


