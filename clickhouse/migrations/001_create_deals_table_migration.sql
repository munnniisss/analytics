CREATE TABLE deals (
    network_name String,
    city_name String,
    company_name String,
    salon_name String,
    manager_name String,
    deal_amount Float64 DEFAULT 0.0,
    from_status String DEFAULT 'EMPTY',
    external_id String,
    to_status String,
    created_at DateTime('Europe/Moscow')
) ENGINE = MergeTree()
ORDER BY (network_name, city_name, company_name, salon_name, manager_name, created_at);
