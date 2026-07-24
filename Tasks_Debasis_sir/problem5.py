#tabular column for different datatypes and their actions

print("-" * 135)

print(f"{'Property':<25}{'List':<12}{'Tuple':<12}{'Set':<12}{'Frozenset':<15}{'Dictionary':<15}")

print("-" * 135)

print(f"{'Syntax':<25}{'[]':<12}{'()':<12}{'{}':<12}{'frozenset()':<15}{'{key:value}':<15}")

print(f"{'Ordered':<25}{'Yes':<12}{'Yes':<12}{'No':<12}{'No':<15}{'Yes':<15}")

print(f"{'Mutable':<25}{'Yes':<12}{'No':<12}{'Yes':<12}{'No':<15}{'Yes':<15}")

print(f"{'Allow Duplicates':<25}{'Yes':<12}{'Yes':<12}{'No':<12}{'No':<15}{'Keys-No':<15}")

print(f"{'Indexed':<25}{'Yes':<12}{'Yes':<12}{'No':<12}{'No':<15}{'Keys-No':<15}")

print(f"{'Heterogeneous':<25}{'Yes':<12}{'Yes':<12}{'Yes':<12}{'Yes':<15}{'Yes':<15}")

print(f"{'Hashable':<25}{'No':<12}{'Yes*':<12}{'No':<12}{'Yes':<15}{'No':<15}")

print(f"{'Can be dictionary key':<25}{'No':<12}{'Yes*':<12}{'No':<12}{'Yes':<15}{'No':<15}")

print(f"{'Can be nested':<25}{'Yes':<12}{'Yes':<12}{'Yes':<12}{'Yes':<15}{'Yes':<15}")

print(f"{'Supports slicing':<25}{'Yes':<12}{'Yes':<12}{'No':<12}{'No':<15}{'No':<15}")

print(f"{'Lookup Speed':<25}{'O(1)':<12}{'O(n)':<12}{'O(1)':<12}{'O(1)':<15}{'O(1)':<15}")

print(f"{'Stores':<25}{'Elements':<12}{'Elements':<12}{'Unique':<12}{'Unique':<15}{'Key-Value':<15}")

print(f"{'Typical Use':<25}{'General':<12}{'Fixed':<12}{'Unique':<12}{'Immutable Set':<15}{'Mapping':<15}")

print("-" * 135)