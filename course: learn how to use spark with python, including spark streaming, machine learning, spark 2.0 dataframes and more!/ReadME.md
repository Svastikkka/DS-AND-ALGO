
## Diffrence between Apache Spark vs Map Reduce
| Feature                | **PySpark (Apache Spark)**                        | **MapReduce (Hadoop)**                    |
| ---------------------- | ------------------------------------------------- | ----------------------------------------- |
| **Language API**       | Python (via PySpark), Scala, Java, R              | Java (primarily)                          |
| **Execution Model**    | In-memory distributed computation                 | Disk-based computation                    |
| **Speed**              | ⚡ Very fast (in-memory processing)                | 🐢 Slower (writes to disk between stages) |
| **Ease of Use**        | High-level APIs (DataFrame, SQL, MLlib)           | Low-level code (map, reduce functions)    |
| **Fault Tolerance**    | RDD lineage (recomputes lost data)                | Replicates intermediate data on HDFS      |
| **Batch vs Streaming** | Supports both batch & streaming                   | Primarily batch processing                |
| **Machine Learning**   | Built-in MLlib library                            | No built-in ML support                    |
| **Cluster Manager**    | Works with YARN, Mesos, Kubernetes, or local      | Usually YARN (Hadoop)                     |
| **Storage**            | Can read from many sources (HDFS, S3, JDBC, etc.) | Usually depends on HDFS                   |

## Installation

```bash
conda create -n pyspark python=3.10
```
```bash
brew install openjdk@11
```

```bash
export JAVA_HOME="/opt/homebrew/opt/openjdk@17"
export PATH="$JAVA_HOME/bin:$PATH"
source ~/.zshrc
java -version
```

```bash
conda install pyspark
```

```python
python -c "import pyspark; print(pyspark.__version__)"
```