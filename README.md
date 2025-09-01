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
  <summary>Click to reveal content</summary>
  
  This is the content that will be hidden by default and revealed when the user clicks the summary.
  You can include any Markdown content here, such as:
  
  * Lists
  * Code blocks
  * **Bold text**
  * *Italic text*
</details>

Place the generated Mermaid output inside a Markdown file:

```---
title: flowchart
---
flowchart TD
  id0("`auth-service`")
  id1("`service-A`")
  id2("`service-B`")
  id3("`db-service`")
  id4("`service-C`")
  id5("`db-service`")
  id6("`payment-gateway`")
  id7("`auth-service`")
  id8("`payment-gateway`")
  id9("`db-service`")
  id10("`service-C`")
  id11("`db-service`")
  id12("`db-service`")
  id13("`service-A`")
  id14("`auth-service`")
  id15("`service-C`")
  id16("`auth-service`")
  id17("`service-B`")
  id18("`service-A`")
  id19("`auth-service`")
  id0 --> id1
  id1 --> id2
  id2 --> id3
  id3 --> id4
  id4 --> id5
  id5 --> id6
  id6 --> id7
  id7 --> id8
  id8 --> id9
  id9 --> id10
  id10 --> id11
  id11 --> id12
  id12 --> id13
  id13 --> id14
  id14 --> id15
  id15 --> id16
  id16 --> id17
  id17 --> id18
  id18 --> id19

```
```

Render with GitHub, VSCode Mermaid preview, or other Mermaid tools.

---

## Project Structure
```
visualizer.py       # Main script
record.py           # Defines Record class
tree.py             # Defines Tree class
```
