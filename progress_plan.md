# StockFlow — 3 Week Scaling Plan

Goal: grow StockFlow into a genuinely capable business system.

---

## Week 1 — Solidify the foundation

**Mon — Unique product IDs**
Replace name-based lookup with real IDs (auto-incrementing). Teaches:
generating IDs safely from existing data, why lookups by unique key
beat lookups by name.
`Commit: "Add unique product IDs"`

**Tue — Input validation pass**
Go through add/update functions across products, customers, sales —
handle bad input (letters where a number's expected, empty required
fields) using `try/except`. Teaches: defensive programming, why
crashing on bad input is a real bug, not an edge case.
`Commit: "Add input validation to product functions"`

**Wed — Same validation pass for customers.py**
Same treatment, different file — should go faster since you're
reusing the pattern from Tuesday.
`Commit: "Add input validation to customer functions"`

**Thu — Same validation pass for sales.py**
Sales is the riskiest file (money + stock) — extra care here on
things like negative quantities or selling more than in stock.
`Commit: "Add input validation and stock checks to sales.py"`

**Fri — Review + refactor day**
Look back at the week. Any duplicated code across products/customers/
sales (e.g. the same "find by ID" loop written 3 times)? Pull it into
a shared helper in `utils.py`. Teaches: recognizing repetition,
DRY (Don't Repeat Yourself) as a real practice, not just a term.
`Commit: "Refactor: extract shared lookup helper into utils.py"`

---

## Week 2 — Add real business value

**Mon — Low-stock alerts**
A function that scans products and flags anything below a threshold
(e.g. quantity < 5). Teaches: list comprehensions, filtering data.
`Commit: "Add low-stock alert function"`

**Tue — Sales reporting: total revenue**
Sum up all sales to show total revenue. Teaches: aggregation,
iterating to accumulate a value.
`Commit: "Add total revenue report"`

**Wed — Sales reporting: best-selling product**
Figure out which product sold the most (by quantity or revenue —
your choice). Teaches: `sorted()` with a `key=`, or building a
tally dict.
`Commit: "Add best-seller report"`

**Thu — Customer purchase history**
Given a customer, show everything they've bought (pulling from
sales data). Teaches: joining data across two lists/files — a real
taste of what relational data feels like before you ever touch a
database.
`Commit: "Add customer purchase history lookup"`

**Fri — Review + menu integration**
Wire all of this week's reports into `main.py`'s menu so it's
actually usable end-to-end, not just functions sitting unused.
`Commit: "Wire reporting functions into main menu"`

---

## Week 3 — Level up the architecture

**Mon — Convert Product to a class**
This is the big one. Refactor the product dict into a `Product`
class with attributes and methods (e.g. `reduce_stock()` becomes a
method on the object itself). Teaches: real OOP, why classes exist
once you've felt dict-passing pain for 2 weeks.
`Commit: "Refactor Product from dict to class"`

**Tue — Convert Customer to a class**
Same treatment, second file — should feel more natural now.
`Commit: "Refactor Customer from dict to class"`

**Wed — Convert Sale to a class**
Same pattern, third file.
`Commit: "Refactor Sale from dict to class"`

**Thu — Update all functions to use the new classes**
Go through products.py/customers.py/sales.py/main.py and make sure
everything works with objects now instead of raw dicts. Expect bugs —
that's normal and useful.
`Commit: "Update CRUD functions to work with class objects"`

**Fri — Final review + README update**
Test the whole system end-to-end. Update README.md to reflect
current features and what's next (maybe SQL/database as the next
big milestone, once you've learned it). Tag this as a milestone
commit.
`Commit: "Week 3 milestone: StockFlow running on OOP architecture"`

---

## After these 3 weeks

Natural next steps, no rush to decide now:

- Move from JSON to a real database (SQLite) once you've learned SQL
- A simple analytics dashboard on top of the reporting functions
- Multi-user or multi-location support

Keep committing daily even on slow days — a small honest commit
("Debug: fix stock validation off-by-one") is still a real commit.
