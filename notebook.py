import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _():
    # from datetime import datetime
    import marimo as mo
    import polars as pl
    from data import fetch_comments_df
    return fetch_comments_df, mo, pl


@app.cell
def _(mo):
    text_input = mo.ui.text(placeholder="Enter Docket ID")
    return (text_input,)


@app.cell
def _(text_input):
    text_input
    return


@app.cell
def _(fetch_comments_df, mo, text_input):
    with mo.status.spinner(title="Fetching comments. Be patient...") as _spinner:
        df = fetch_comments_df(docket_id=text_input.value)
    return (df,)


@app.cell
def _(df, mo):
    mo.stop(df.is_empty(), mo.md("No data in yet, type DocketID above."))
    return


@app.cell
def _(df, mo):
    mo.md(f"**Fetched {len(df):,} comments!**")
    return


@app.cell
def _(mo):
    mo.md(r"""## Raw Data Explorer""")
    return


@app.cell
def _(df, mo):
    mo.stop(df.is_empty(), mo.md("No data to explore yet..."))
    return


@app.cell
def _(df, pl):
    (
        df.select(pl.col("docketId"), pl.col("agencyId"), pl.col("firstName"), pl.col("lastName"), pl.col("modifyDate"), pl.col("comment"), pl.col("commentID"))
    )
    return


@app.cell
def _(df, pl):
    df_filt = (
        df
        .group_by('commentID').agg(pl.len(), pl.col("comment"), pl.col("modifyDate"))
        .filter(pl.col("len") > 1)
        .sort(by="len", descending=True)
    )
    return (df_filt,)


@app.cell
def _(df_filt):
    choices_dict = {
        row["commentID"]: row["len"] for row in df_filt.iter_rows(named=True) if row["commentID"] if row["commentID"] != "null"
    }
    return (choices_dict,)


@app.cell
def _(choices_dict, mo):
    dropdown_dict = mo.ui.dropdown(options=choices_dict, value=list(choices_dict.keys())[0], label="Choose comment ID")
    return (dropdown_dict,)


@app.cell
def _(mo):
    mo.md(r"""## Duplicate Posts Explorer""")
    return


@app.cell
def _(df, mo):
    mo.stop(df.is_empty(), mo.md("No posts to explore yet..."))
    return


@app.cell
def _(dropdown_dict, mo):
    mo.hstack(
        [dropdown_dict, mo.md(f"Number of repeats: {dropdown_dict.value}")]
    )
    return


@app.cell
def _(df_filt, dropdown_dict, pl):
    sel_text = (
        df_filt
        .filter(pl.col('commentID') == dropdown_dict.selected_key)
        .explode(pl.col("modifyDate"), pl.col("comment"))
        .sort(by="modifyDate")
        .with_columns(
            pl.col("modifyDate").dt.strftime("%B %d, %Y at %I:%M %p UTC")
        )
    )
    return (sel_text,)


@app.cell
def _(mo, sel_text):
    sel_rows = [f"DATE:{row['modifyDate']}\nTEXT:{row['comment']}" for row in sel_text.iter_rows(named=True)]
    text = "\n\n====\n\n".join(sel_rows[0:100])
    mo.ui.text_area(value=text, rows=100)
    return sel_rows, text


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
