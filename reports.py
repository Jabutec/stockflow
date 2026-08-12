
def sales_summary(sales):
    total_revenue = sum(sale["total"] for sale in sales)
    total_sales = len(sales)
    
    average_sales = (
        total_revenue/total_sales
        if total_sales>0
        else 0
                                    
    )
    
    return total_sales,total_revenue,average_sales