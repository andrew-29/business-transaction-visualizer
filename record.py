class Record:
    """A record of a  transaction/request

    Attributes:
        name: business trace service entity name
        trace_id: a unique identifier assigned to a request
        parent_id: the trace_id of a the parent request
        duration: the time it took a request to be processed (ms)
        start_time: the time at which the request was opened
        end_time: the time at which the request was ended

    Representation Invariants:
        - len(self.duration) > 0
    """

    name: str
    trace_id: str
    span_id: str
    parent_id: str
    duration: int
    start_time: str
    end_time: str
    mermaid_id: str

    def __init__(self, name: str, trace_id: str, span_id: str, parent_id: str, duration: int, start_time: str, end_time: str, mermaid_id: str) -> None:
        """Initialize a new record
        """
        self.name = f"\"`{name.replace(' ', '')}`\""
        self.trace_id = trace_id
        self.parent_id = parent_id
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time
        self.span_id = span_id
        self.mermaid_id = mermaid_id
