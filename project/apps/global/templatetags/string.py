from django import template


register = template.Library()


@register.filter(name='split') 
def split(value: str, delimiter=',') -> list[str]:
    """
    Splits a given string into a list using the specified delimiter.

    Parameters
    ----------
    value : str
        The input string to be split.
    delimiter : str, optional
        The character or string used as the delimiter (default is ',').

    Returns
    -------
    list
        A list of substrings obtained by splitting the input string.

    Examples
    --------
    In a Django template:

    ```django
    {% load string %}
    
    {% for item in 'apple,banana,grape'|split:',' %}
        <p>{{ item }}</p>
    {% endfor %}
    ```

    If `value` is `'apple,banana,grape'` and `delimiter` is `','`, 
    the output will be:
    
    ```python
    ['apple', 'banana', 'grape']
    ```

    Notes
    -----
    - If the delimiter is not found in the string, the function returns a single-element list containing the original string.
    """
    return value.split(delimiter)