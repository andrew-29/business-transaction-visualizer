# Visualizer

A Python-based tool for transforming trace/span records into hierarchical tree structures and Mermaid.js flowcharts.

---

## Features
- Load records from a JSON file.
- Convert raw dictionaries into `Record` objects.
- Build a hierarchical `Tree` of spans using parent-child relationships.
- Generate a Mermaid flowchart (`flowchart TD`) representation for visualization.
- Print tree structure in plain text.

---

## Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/visualizer.git
cd visualizer

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
- `mermaid-builder`
- `mermaid`
- Python 3.8+

---

## Usage

### Input JSON Format
Your JSON file should contain a list of records under the key `records`:

```json
{
  "records": [
    {
      "dt.entity.service.entity.name": "service-A",
      "trace.id": "t1",
      "span.id": "s1",
      "span.parent_id": null,
      "duration": 120,
      "start_time": "2023-01-01T00:00:00Z",
      "end_time": "2023-01-01T00:00:02Z"
    },
    {
      "dt.entity.service.entity.name": "service-B",
      "trace.id": "t1",
      "span.id": "s2",
      "span.parent_id": "s1",
      "duration": 60,
      "start_time": "2023-01-01T00:00:01Z",
      "end_time": "2023-01-01T00:00:02Z"
    }
  ]
}
```

### Run
```bash
python visualizer.py input.json
```

### Output
1. Prints number of records loaded.
2. Prints parent-child relationships during flowchart generation.
3. Outputs a Mermaid flowchart string:

```
flowchart TD
    id0[service-A]
    id1[service-B]
    id0 --> id1
```

This string can be used in Markdown or Mermaid-compatible viewers.

---

## Example: Visualizing with Mermaid
Download a JSON representation of your business transactions

<details>
  <summary>Click to view example JSON file</summary>
```
  {
    "records": [
        {
            "dt.entity.service.entity.name": "auth-service",
            "trace.id": "t1",
            "span.id": "s1",
            "span.parent_id": null,
            "duration": 157,
            "start_time": "2023-01-01T00:00:10Z",
            "end_time": "2023-01-01T00:00:10.157000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t1",
            "span.id": "s2",
            "span.parent_id": "s1",
            "duration": 103,
            "start_time": "2023-01-01T00:00:10.154000Z",
            "end_time": "2023-01-01T00:00:10.257000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t1",
            "span.id": "s3",
            "span.parent_id": "s2",
            "duration": 266,
            "start_time": "2023-01-01T00:00:10.244000Z",
            "end_time": "2023-01-01T00:00:10.510000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t1",
            "span.id": "s4",
            "span.parent_id": "s1",
            "duration": 238,
            "start_time": "2023-01-01T00:00:10.152000Z",
            "end_time": "2023-01-01T00:00:10.390000Z"
        },
        {
            "dt.entity.service.entity.name": "service-B",
            "trace.id": "t1",
            "span.id": "s5",
            "span.parent_id": "s4",
            "duration": 146,
            "start_time": "2023-01-01T00:00:10.272000Z",
            "end_time": "2023-01-01T00:00:10.418000Z"
        },
        {
            "dt.entity.service.entity.name": "service-D",
            "trace.id": "t1",
            "span.id": "s6",
            "span.parent_id": "s4",
            "duration": 208,
            "start_time": "2023-01-01T00:00:10.208000Z",
            "end_time": "2023-01-01T00:00:10.416000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t1",
            "span.id": "s7",
            "span.parent_id": "s1",
            "duration": 215,
            "start_time": "2023-01-01T00:00:10.072000Z",
            "end_time": "2023-01-01T00:00:10.287000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t1",
            "span.id": "s8",
            "span.parent_id": "s7",
            "duration": 172,
            "start_time": "2023-01-01T00:00:10.213000Z",
            "end_time": "2023-01-01T00:00:10.385000Z"
        },
        {
            "dt.entity.service.entity.name": "service-D",
            "trace.id": "t1",
            "span.id": "s9",
            "span.parent_id": "s7",
            "duration": 95,
            "start_time": "2023-01-01T00:00:10.253000Z",
            "end_time": "2023-01-01T00:00:10.348000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t1",
            "span.id": "s10",
            "span.parent_id": "s7",
            "duration": 241,
            "start_time": "2023-01-01T00:00:10.259000Z",
            "end_time": "2023-01-01T00:00:10.500000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t2",
            "span.id": "s11",
            "span.parent_id": null,
            "duration": 233,
            "start_time": "2023-01-01T00:00:20Z",
            "end_time": "2023-01-01T00:00:20.233000Z"
        },
        {
            "dt.entity.service.entity.name": "payment-gateway",
            "trace.id": "t2",
            "span.id": "s12",
            "span.parent_id": "s11",
            "duration": 135,
            "start_time": "2023-01-01T00:00:20.194000Z",
            "end_time": "2023-01-01T00:00:20.329000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t2",
            "span.id": "s13",
            "span.parent_id": "s12",
            "duration": 157,
            "start_time": "2023-01-01T00:00:20.284000Z",
            "end_time": "2023-01-01T00:00:20.441000Z"
        },
        {
            "dt.entity.service.entity.name": "auth-service",
            "trace.id": "t2",
            "span.id": "s14",
            "span.parent_id": "s13",
            "duration": 300,
            "start_time": "2023-01-01T00:00:20.327000Z",
            "end_time": "2023-01-01T00:00:20.627000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t2",
            "span.id": "s15",
            "span.parent_id": "s13",
            "duration": 196,
            "start_time": "2023-01-01T00:00:20.300000Z",
            "end_time": "2023-01-01T00:00:20.496000Z"
        },
        {
            "dt.entity.service.entity.name": "service-B",
            "trace.id": "t2",
            "span.id": "s16",
            "span.parent_id": "s13",
            "duration": 125,
            "start_time": "2023-01-01T00:00:20.299000Z",
            "end_time": "2023-01-01T00:00:20.424000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t2",
            "span.id": "s17",
            "span.parent_id": "s12",
            "duration": 137,
            "start_time": "2023-01-01T00:00:20.313000Z",
            "end_time": "2023-01-01T00:00:20.450000Z"
        },
        {
            "dt.entity.service.entity.name": "auth-service",
            "trace.id": "t2",
            "span.id": "s18",
            "span.parent_id": "s17",
            "duration": 99,
            "start_time": "2023-01-01T00:00:20.448000Z",
            "end_time": "2023-01-01T00:00:20.547000Z"
        },
        {
            "dt.entity.service.entity.name": "auth-service",
            "trace.id": "t2",
            "span.id": "s19",
            "span.parent_id": "s11",
            "duration": 203,
            "start_time": "2023-01-01T00:00:20.046000Z",
            "end_time": "2023-01-01T00:00:20.249000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t2",
            "span.id": "s20",
            "span.parent_id": "s19",
            "duration": 178,
            "start_time": "2023-01-01T00:00:20.096000Z",
            "end_time": "2023-01-01T00:00:20.274000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t2",
            "span.id": "s21",
            "span.parent_id": "s20",
            "duration": 128,
            "start_time": "2023-01-01T00:00:20.199000Z",
            "end_time": "2023-01-01T00:00:20.327000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t2",
            "span.id": "s22",
            "span.parent_id": "s19",
            "duration": 82,
            "start_time": "2023-01-01T00:00:20.137000Z",
            "end_time": "2023-01-01T00:00:20.219000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t2",
            "span.id": "s23",
            "span.parent_id": "s22",
            "duration": 287,
            "start_time": "2023-01-01T00:00:20.196000Z",
            "end_time": "2023-01-01T00:00:20.483000Z"
        },
        {
            "dt.entity.service.entity.name": "service-D",
            "trace.id": "t2",
            "span.id": "s24",
            "span.parent_id": "s22",
            "duration": 216,
            "start_time": "2023-01-01T00:00:20.147000Z",
            "end_time": "2023-01-01T00:00:20.363000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t2",
            "span.id": "s25",
            "span.parent_id": "s11",
            "duration": 101,
            "start_time": "2023-01-01T00:00:20.028000Z",
            "end_time": "2023-01-01T00:00:20.129000Z"
        },
        {
            "dt.entity.service.entity.name": "auth-service",
            "trace.id": "t2",
            "span.id": "s26",
            "span.parent_id": "s25",
            "duration": 166,
            "start_time": "2023-01-01T00:00:20.121000Z",
            "end_time": "2023-01-01T00:00:20.287000Z"
        },
        {
            "dt.entity.service.entity.name": "service-D",
            "trace.id": "t2",
            "span.id": "s27",
            "span.parent_id": "s26",
            "duration": 107,
            "start_time": "2023-01-01T00:00:20.212000Z",
            "end_time": "2023-01-01T00:00:20.319000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t3",
            "span.id": "s28",
            "span.parent_id": null,
            "duration": 195,
            "start_time": "2023-01-01T00:00:30Z",
            "end_time": "2023-01-01T00:00:30.195000Z"
        },
        {
            "dt.entity.service.entity.name": "service-C",
            "trace.id": "t3",
            "span.id": "s29",
            "span.parent_id": "s28",
            "duration": 261,
            "start_time": "2023-01-01T00:00:30.047000Z",
            "end_time": "2023-01-01T00:00:30.308000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t3",
            "span.id": "s30",
            "span.parent_id": "s29",
            "duration": 202,
            "start_time": "2023-01-01T00:00:30.242000Z",
            "end_time": "2023-01-01T00:00:30.444000Z"
        },
        {
            "dt.entity.service.entity.name": "db-service",
            "trace.id": "t3",
            "span.id": "s31",
            "span.parent_id": "s28",
            "duration": 270,
            "start_time": "2023-01-01T00:00:30.040000Z",
            "end_time": "2023-01-01T00:00:30.310000Z"
        },
        {
            "dt.entity.service.entity.name": "service-B",
            "trace.id": "t3",
            "span.id": "s32",
            "span.parent_id": "s31",
            "duration": 204,
            "start_time": "2023-01-01T00:00:30.283000Z",
            "end_time": "2023-01-01T00:00:30.487000Z"
        },
        {
            "dt.entity.service.entity.name": "payment-gateway",
            "trace.id": "t3",
            "span.id": "s33",
            "span.parent_id": "s28",
            "duration": 147,
            "start_time": "2023-01-01T00:00:30.111000Z",
            "end_time": "2023-01-01T00:00:30.258000Z"
        },
        {
            "dt.entity.service.entity.name": "service-A",
            "trace.id": "t3",
            "span.id": "s34",
            "span.parent_id": "s33",
            "duration": 217,
            "start_time": "2023-01-01T00:00:30.197000Z",
            "end_time": "2023-01-01T00:00:30.414000Z"
        },
        {
            "dt.entity.service.entity.name": "service-D",
            "trace.id": "t4",
            "span.id": "s35",
            "span.parent_id": null,
            "duration": 264,
            "start_time": "2023-01-01T00:00:40Z",
            "end_time": "2023-01-01T00:00:40.264000Z"
        },
...
```
</details>

Place the generated Mermaid output inside a Markdown file:

```---
title: flowchart
---
flowchart TD
  id0("`auth-service`")
  id1("`service-A`")
  id2("`db-service`")
  id3("`db-service`")
  id4("`service-B`")
  id5("`service-D`")
  id6("`service-C`")
  id7("`service-C`")
  id8("`service-D`")
  id9("`service-C`")
  id0 --> id1
  id1 --> id2
  id0 --> id3
  id3 --> id4
  id3 --> id5
  id0 --> id6
  id6 --> id7
  id6 --> id8
  id6 --> id9

```


Render with GitHub, VSCode Mermaid preview, or other Mermaid tools.

---

## Project Structure
```
visualizer.py       # Main script
record.py           # Defines Record class
tree.py             # Defines Tree class
```
