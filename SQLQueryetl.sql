select * from Housing
order by average_room_size desc

select top 10  * from Housing
order by price desc

select top 10 * from Housing
order by area desc


select * from Housing
order by  price_per_sqft desc

select * from Housing
where lux between 2 and 4
order by lux desc

select * from housing
where furnishingstatus='furnished' and bedrooms between 1  and 2 

select * from Housing
where furnishingstatus='furnished' 
order by price desc

select * from Housing
where furnishingstatus='semi-furnished'
order by price desc

select * from Housing
where furnishingstatus='unfurnished'
order by price desc

select top 10 * from Housing
order by parking desc


select top 10 * from Housing 
order by lux asc

select top 10 * from Housing
order by parking_bedroom asc

