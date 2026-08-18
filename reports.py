
def sales_summary(sales):
    total_revenue = sum(sale["total"] for sale in sales)
    total_sales = len(sales)
    
    average_sales = (
        total_revenue/total_sales
        if total_sales>0
        else 0
                                    
    )
    
    return total_sales,total_revenue,average_sales

def generate_report(sales):
    result = sales_summary(sales)
    print("-------Report--------")
    print(f"Total Sales: {result[0]}")
    print(f"Total Revenue: {result[1]}")
    print(f"Average Sales: {result[2]}")
    
    