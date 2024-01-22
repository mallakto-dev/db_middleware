CREATE TABLE orders (
order_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
user_id BIGINT,
order_items TEXT,
order_type VARCHAR(255),
order_status VARCHAR(255),
created_at DATE,
total_cost BIGINT,
user_name VARCHAR(255),
user_phone VARCHAR(255),
user_address VARCHAR(255)
);