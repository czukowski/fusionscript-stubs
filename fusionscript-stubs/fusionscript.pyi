from typing import Annotated, Any, Final, List, NotRequired, Optional, TypedDict
from typing import overload
from typing_extensions import Literal
from dataclasses import dataclass
from deprecated import deprecated

@dataclass
class ValueRange:
    min: int
    max: int


ColorSet1 = Literal['Orange', 'Apricot', 'Yellow', 'Lime', 'Olive', 'Green', 'Teal', 'Navy', 'Blue', 'Purple', 'Violet', 'Pink', 'Tan', 'Beige', 'Brown', 'Chocolate']
ColorSet2 = Literal['Blue', 'Cyan', 'Green', 'Yellow', 'Red', 'Pink', 'Purple', 'Fuchsia', 'Rose', 'Lavender', 'Sky', 'Mint', 'Lemon', 'Sand', 'Cocoa', 'Cream']

ClipColor = ColorSet1
FlagColor = ColorSet2
MarkerColor = ColorSet2

GalleryStillExportFormat = Literal['dpx', 'cin', 'tif', 'jpg', 'png', 'ppm', 'bmp', 'xpm']

GradeMode = Literal[0, 1, 2]
""" 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned" """

KeyframeMode = Literal[
    Resolve.KEYFRAME_MODE_ALL,
    Resolve.KEYFRAME_MODE_COLOR,
    Resolve.KEYFRAME_MODE_SIZING,
]

LUTExportType = Literal[
    Resolve.EXPORT_LUT_17PTCUBE,
    Resolve.EXPORT_LUT_33PTCUBE,
    Resolve.EXPORT_LUT_65PTCUBE,
    Resolve.EXPORT_LUT_PANASONICVLUT,
]

MagicMaskMode = Literal['F', 'B', 'BI']
""" 'F' - forward, 'B' - backward, 'BI' - bidirection """

MediaType = Literal[1, 2]
""" 1 - Video only, 2 - Audio only """

PageName = Literal['media', 'cut', 'edit', 'fusion', 'color', 'fairlight', 'deliver']

RenderMode = Literal[0, 1]
""" 0 - Individual clips, 1 - Single clip """

StereoEye = Literal['left', 'right']

StillFrameSource = Literal[1, 2]
""" 1 - First frame, 2 - Middle frame """

SubTrackType = Literal['mono', 'stereo', '5.1', '5.1film', '7.1', '7.1film'] + ['adaptive{number}'.format(number) for number in range(1, 24)]

TimelineExportType = Literal[
    Resolve.EXPORT_AAF,
    Resolve.EXPORT_DRT,
    Resolve.EXPORT_EDL,
    Resolve.EXPORT_FCP_7_XML,
    Resolve.EXPORT_FCPXML_1_8,
    Resolve.EXPORT_FCPXML_1_9,
    Resolve.EXPORT_FCPXML_1_10,
    Resolve.EXPORT_HDR_10_PROFILE_A,
    Resolve.EXPORT_HDR_10_PROFILE_B,
    Resolve.EXPORT_TEXT_CSV,
    Resolve.EXPORT_TEXT_TAB,
    Resolve.EXPORT_DOLBY_VISION_VER_2_9,
    Resolve.EXPORT_DOLBY_VISION_VER_4_0,
    Resolve.EXPORT_DOLBY_VISION_VER_5_1,
    Resolve.EXPORT_OTIO,
    Resolve.EXPORT_ALE,
    Resolve.EXPORT_ALE_CDL,
]

TimelineExportSubtype = Literal[
    Resolve.EXPORT_NONE,
    Resolve.EXPORT_AAF_NEW,
    Resolve.EXPORT_AAF_EXISTING,
    Resolve.EXPORT_CDL,
    Resolve.EXPORT_SDL,
    Resolve.EXPORT_MISSING_CLIPS,
]

TrackType = Literal['audio', 'video', 'subtitle']

UniqueFilenameStyle = Literal[0, 1]
""" 0 - Prefix, 1 - Suffix """

VersionType = Literal[0, 1]
""" 0 - Local, 1 - Remote """

AutoCaptionSettings = TypedDict('AutoCaptionSettings', {
    Resolve.SUBTITLE_LANGUAGE: Literal[Resolve.AUTO_CAPTION_AUTO, \
                                       Resolve.AUTO_CAPTION_DANISH, \
                                       Resolve.AUTO_CAPTION_DUTCH, \
                                       Resolve.AUTO_CAPTION_ENGLISH, \
                                       Resolve.AUTO_CAPTION_FRENCH, \
                                       Resolve.AUTO_CAPTION_GERMAN, \
                                       Resolve.AUTO_CAPTION_ITALIAN, \
                                       Resolve.AUTO_CAPTION_JAPANESE, \
                                       Resolve.AUTO_CAPTION_KOREAN, \
                                       Resolve.AUTO_CAPTION_MANDARIN_SIMPLIFIED, \
                                       Resolve.AUTO_CAPTION_MANDARIN_TRADITIONAL, \
                                       Resolve.AUTO_CAPTION_NORWEGIAN, \
                                       Resolve.AUTO_CAPTION_PORTUGUESE, \
                                       Resolve.AUTO_CAPTION_RUSSIAN, \
                                       Resolve.AUTO_CAPTION_SPANISH, \
                                       Resolve.AUTO_CAPTION_SWEDISH],
    Resolve.SUBTITLE_CAPTION_PRESET: Resolve.AUTO_CAPTION_SUBTITLE_DEFAULT | Resolve.AUTO_CAPTION_TELETEXT | Resolve.AUTO_CAPTION_NETFLIX,
    Resolve.SUBTITLE_CHARS_PER_LINE: Annotated[int, ValueRange(1, 60)],
    Resolve.SUBTITLE_LINE_BREAK: Literal[Resolve.AUTO_CAPTION_LINE_SINGLE, Resolve.AUTO_CAPTION_LINE_DOUBLE],
    Resolve.SUBTITLE_GAP: Annotated[int, ValueRange(0, 10)],
})

CloudProjectsSettings = TypedDict('CloudProjectsSettings', {
    Resolve.CLOUD_SETTING_PROJECT_NAME: str,
    Resolve.CLOUD_SETTING_PROJECT_MEDIA_PATH: str,
    Resolve.CLOUD_SETTING_IS_COLLAB: bool,
    Resolve.CLOUD_SETTING_SYNC_MODE: Literal[Resolve.CLOUD_SYNC_NONE, Resolve.CLOUD_SYNC_PROXY_ONLY, Resolve.CLOUD_SYNC_PROXY_AND_ORIG],
    Resolve.CLOUD_SETTING_IS_CAMERA_ACCESS: bool,
})


class CDLMap(TypedDict):
    """ Keys of map are: "NodeIndex", "Slope", "Offset", "Power", "Saturation", where 1 <= NodeIndex <= total number of nodes. """
    NodeIndex: int
    Slope: str
    Offset: str
    Power: str
    Saturation: str


class DbInfo(TypedDict):
    """
    Keys:
     - 'DbType': 'Disk' or 'PostgreSQL' (string)
     - 'DbName': database name (string)
     - 'IpAddress': IP address of the PostgreSQL server (string, optional key - defaults to '127.0.0.1')
    """
    DbType: Literal['Disk', 'PostgreSQL']
    DbName: str
    IpAddress: NotRequired[str]


class FloatingWindowParams(TypedDict):
    left: Any
    right: Any
    top: Any
    bottom: Any


class ImportClipInfo(TypedDict):
    FilePath: str
    StartIndex: int
    EndIndex: int


class Marker(TypedDict):
    color: MarkerColor
    duration: float
    note: str
    name: str
    customData: str


class MediaPoolClipInfo(TypedDict):
    """
    Keys:
     - 'mediaPoolItem'
     - 'startFrame' (int)
     - 'endFrame' (int)
     - (optional) 'mediaType' (int; 1 - Video only, 2 - Audio only)
     - 'trackIndex' (int)
     - 'recordFrame' (int)
    """
    mediaPoolItem: MediaPoolItem
    startFrame: int
    endFrame: int
    mediaType: NotRequired[MediaType]
    trackIndex: int
    recordFrame: int


class MediaPoolItemInfo(TypedDict):
    media: str
    startFrame: int
    endFrame: int


class NewTrackOptions(TypedDict):
    audiotype: SubTrackType
    index: int


class Preset(TypedDict):
    """ No documentation available """
    pass


class RenderPreset(TypedDict):
    """ No documentation available """
    pass


class RenderSettings(TypedDict):
    """
    Notes about some of the keys:
     - 'SelectAllFrames' - When set True, the settings MarkIn and MarkOut are ignored
     - 'UniqueFilenameStyle' - 0 - Prefix, 1 - Suffix
     - 'FrameRate' - Examples: 23.976, 24
     - 'PixelAspectRatio' - For SD resolution: "16_9" or "4_3" (other resolutions: "square" or "cinemascope")
     - 'VideoQuality' - Possible values for current codec (if applicable):
        * 0 (int) - will set quality to automatic
        * [1 -> MAX] (int) - will set input bit rate
        * ["Least", "Low", "Medium", "High", "Best"] (String) - will set input quality level
     - 'AudioCodec' - Example: "aac"
     - 'ColorSpaceTag' - Example: "Same as Project", "AstroDesign"
     - 'GammaTag' - Example: "Same as Project", "ACEScct"
     - 'EncodingProfile' - Example: "Main10". Can only be set for H.264 and H.265.
     - 'MultiPassEncode' - Can only be set for H.264.
     - 'AlphaMode' - 0 - Premultiplied, 1 - Straight. Can only be set if "ExportAlpha" is true.
     - 'NetworkOptimization' - Only supported by QuickTime and MP4 formats.
    """
    SelectAllFrames: bool
    MarkIn: int
    MarkOut: int
    TargetDir: str
    CustomName: str
    UniqueFilenameStyle: Literal[0, 1]
    ExportVideo: bool
    ExportAudio: bool
    FormatWidth: int
    FormatHeight: int
    FrameRate: float
    PixelAspectRatio: str
    VideoQuality: str | int
    AudioCodec: str
    AudioBitDepth: int
    AudioSampleRate: int
    ColorSpaceTag : str
    GammaTag : str
    ExportAlpha: bool
    EncodingProfile: str
    MultiPassEncode: bool
    AlphaMode: Literal[0, 1]
    NetworkOptimization: bool


class RenderResolution(TypedDict):
    Width: int
    Height: int


class RenderFormatAndCodec(TypedDict):
    format: str
    codec: str


class RenderJob(TypedDict):
    """ No documentation available """
    pass


class RenderJobStatus(TypedDict):
    """ No documentation available """
    pass


class TakeInfo(TypedDict):
    """ Keys: 'startFrame', 'endFrame' and 'mediaPoolItem' """
    startFrame: int
    endFrame: int
    mediaPoolItem: MediaPoolItem


class ThumbnailData(TypedDict):
    """ Keys: 'width', 'height', 'format' and 'data' """
    width: int
    height: int
    format: str
    data: str


class TimelineClipInfo(TypedDict):
    """ Example: {'startTimecode' : '00:00:00:00', 'name' : 'Compound Clip 1'}. """
    startTimecode: str
    name: str


class TimelineImportOptions(TypedDict):
    """
    Keys:
     - 'timelineName': string, specifies the name of the timeline to be created. Not valid for DRT import
     - 'importSourceClips': bool, specifies whether source clips should be imported, True by default. Not valid for DRT import
     - 'sourceClipsPath': string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "importSourceClips" is True
     - 'sourceClipsFolders': List of Media Pool folder objects to search for source clips if the media is not present in current folder and if "importSourceClips" is False. Not valid for DRT import
     - 'interlaceProcessing': Bool, specifies whether to enable interlace processing on the imported timeline being created. valid only for AAF import
    """
    timelineName: str
    importSourceClips: bool
    sourceClipsPath: str
    sourceClipsFolders: List[Folder]
    interlaceProcessing: bool


class TimelineItemsImportOptions(TypedDict):
    """
    Keys:
     - 'autoImportSourceClipsIntoMediaPool': Bool, specifies if source clips should be imported into media pool, True by default
     - 'ignoreFileExtensionsWhenMatching': Bool, specifies if file extensions should be ignored when matching, False by default
     - 'linkToSourceCameraFiles': Bool, specifies if link to source camera files should be enabled, False by default
     - 'useSizingInfo': Bool, specifies if sizing information should be used, False by default
     - 'importMultiChannelAudioTracksAsLinkedGroups': Bool, specifies if multi-channel audio tracks should be imported as linked groups, False by default
     - 'insertAdditionalTracks': Bool, specifies if additional tracks should be inserted, True by default
     - 'insertWithOffset': string, specifies insert with offset value in timecode format - defaults to "00:00:00:00", applicable if 'insertAdditionalTracks' is False
     - 'sourceClipsPath': string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if 'ignoreFileExtensionsWhenMatching' is True
     - 'sourceClipsFolders': string, list of Media Pool folder objects to search for source clips if the media is not present in current folder
    """
    autoImportSourceClipsIntoMediaPool: NotRequired[bool]
    ignoreFileExtensionsWhenMatching: NotRequired[bool]
    linkToSourceCameraFiles: NotRequired[bool]
    useSizingInfo: NotRequired[bool]
    importMultiChannelAudioTracksAsLinkedGroups: NotRequired[bool]
    insertAdditionalTracks: NotRequired[bool]
    insertWithOffset: NotRequired[str]
    sourceClipsPath: NotRequired[str]
    sourceClipsFolders: NotRequired[str]


DYNAMIC_ZOOM_EASE_LINEAR: Final = 0
DYNAMIC_ZOOM_EASE_IN: Final
DYNAMIC_ZOOM_EASE_OUT: Final
DYNAMIC_ZOOM_EASE_IN_AND_OUT: Final

COMPOSITE_NORMAL: Final = 0
COMPOSITE_ADD: Final
COMPOSITE_SUBTRACT: Final
COMPOSITE_DIFF: Final
COMPOSITE_MULTIPLY: Final
COMPOSITE_SCREEN: Final
COMPOSITE_OVERLAY: Final
COMPOSITE_HARDLIGHT: Final
COMPOSITE_SOFTLIGHT: Final
COMPOSITE_DARKEN: Final
COMPOSITE_LIGHTEN: Final
COMPOSITE_COLOR_DODGE: Final
COMPOSITE_COLOR_BURN: Final
COMPOSITE_EXCLUSION: Final
COMPOSITE_HUE: Final
COMPOSITE_SATURATE: Final
COMPOSITE_COLORIZE: Final
COMPOSITE_LUMA_MASK: Final
COMPOSITE_DIVIDE: Final
COMPOSITE_LINEAR_DODGE: Final
COMPOSITE_LINEAR_BURN: Final
COMPOSITE_LINEAR_LIGHT: Final
COMPOSITE_VIVID_LIGHT: Final
COMPOSITE_PIN_LIGHT: Final
COMPOSITE_HARD_MIX: Final
COMPOSITE_LIGHTER_COLOR: Final
COMPOSITE_DARKER_COLOR: Final
COMPOSITE_FOREGROUND: Final
COMPOSITE_ALPHA: Final
COMPOSITE_INVERTED_ALPHA: Final
COMPOSITE_LUM: Final
COMPOSITE_INVERTED_LUM: Final

RETIME_USE_PROJECT: Final = 0
RETIME_NEAREST: Final
RETIME_FRAME_BLEND: Final
RETIME_OPTICAL_FLOW: Final

MOTION_EST_USE_PROJECT: Final = 0
MOTION_EST_STANDARD_FASTER: Final
MOTION_EST_STANDARD_BETTER: Final
MOTION_EST_ENHANCED_FASTER: Final
MOTION_EST_ENHANCED_BETTER: Final
MOTION_EST_SPEED_WARP_BETTER: Final
MOTION_EST_SPEED_WARP_FASTER: Final

SCALE_USE_PROJECT: Final = 0
SCALE_CROP: Final
SCALE_FIT: Final
SCALE_FILL: Final
SCALE_STRETCH: Final

RESIZE_FILTER_USE_PROJECT: Final = 0
RESIZE_FILTER_SHARPER: Final
RESIZE_FILTER_SMOOTHER: Final
RESIZE_FILTER_BICUBIC: Final
RESIZE_FILTER_BILINEAR: Final
RESIZE_FILTER_BESSEL: Final
RESIZE_FILTER_BOX: Final
RESIZE_FILTER_CATMULL_ROM: Final
RESIZE_FILTER_CUBIC: Final
RESIZE_FILTER_GAUSSIAN: Final
RESIZE_FILTER_LANCZOS: Final
RESIZE_FILTER_MITCHELL: Final
RESIZE_FILTER_NEAREST_NEIGHBOR: Final
RESIZE_FILTER_QUADRATIC: Final
RESIZE_FILTER_SINC: Final
RESIZE_FILTER_LINEAR: Final


class Resolve:
    """
    List and Dict Data Structures
    -----------------------------
    Beside primitive data types, Resolve's Python API mainly uses list and dict data structures. Lists are denoted by [ ... ] and dicts are denoted by { ... } above.
    As Lua does not support list and dict data structures, the Lua API implements "list" as a table with indices, e.g. { [1] = listValue1, [2] = listValue2, ... }.
    Similarly the Lua API implements "dict" as a table with the dictionary key as first element, e.g. { [dictKey1] = dictValue1, [dictKey2] = dictValue2, ... }.

    Keyframe Mode information
    -------------------------
    This section covers additional notes for the functions Resolve.GetKeyframeMode() and Resolve.SetKeyframeMode(keyframeMode).

    'keyframeMode' can be one of the following enums:
        - resolve.KEYFRAME_MODE_ALL     == 0
        - resolve.KEYFRAME_MODE_COLOR   == 1
        - resolve.KEYFRAME_MODE_SIZING  == 2

    Integer values returned by Resolve.GetKeyframeMode() will correspond to the enums above.

    Cloud Projects Settings
    --------------------------------------
    This section covers additional notes for the functions "ProjectManager:CreateCloudProject," "ProjectManager:ImportCloudProject," and "ProjectManager:RestoreCloudProject"

    All three functions take in a {cloudSettings} dict, that have the following keys:
    * resolve.CLOUD_SETTING_PROJECT_NAME: String, ["" by default]
    * resolve.CLOUD_SETTING_PROJECT_MEDIA_PATH: String, ["" by default]
    * resolve.CLOUD_SETTING_IS_COLLAB: Bool, [False by default]
    * resolve.CLOUD_SETTING_SYNC_MODE: syncMode (see below), [resolve.CLOUD_SYNC_PROXY_ONLY by default]
    * resolve.CLOUD_SETTING_IS_CAMERA_ACCESS: Bool [False by default]

    Where syncMode is one of the following values:
    * resolve.CLOUD_SYNC_NONE,
    * resolve.CLOUD_SYNC_PROXY_ONLY,
    * resolve.CLOUD_SYNC_PROXY_AND_ORIG

    All three "ProjectManager:CreateCloudProject," "ProjectManager:ImportCloudProject," and "ProjectManager:RestoreCloudProject" require resolve.PROJECT_MEDIA_PATH to be defined. "ProjectManager:CreateCloudProject" also requires resolve.PROJECT_NAME to be defined.

    Looking up Project and Clip properties
    --------------------------------------
    This section covers additional notes for the functions "Project:GetSetting", "Project:SetSetting", "Timeline:GetSetting", "Timeline:SetSetting", "MediaPoolItem:GetClipProperty" and
    "MediaPoolItem:SetClipProperty". These functions are used to get and set properties otherwise available to the user through the Project Settings and the Clip Attributes dialogs.

    The functions follow a key-value pair format, where each property is identified by a key (the settingName or propertyName parameter) and possesses a value (typically a text value). Keys and values are
    designed to be easily correlated with parameter names and values in the Resolve UI. Explicitly enumerated values for some parameters are listed below.

    Some properties may be read only - these include intrinsic clip properties like date created or sample rate, and properties that can be disabled in specific application contexts (e.g. custom colorspaces
    in an ACES workflow, or output sizing parameters when behavior is set to match timeline)

    Getting values:
    Invoke "Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" with the appropriate property key. To get a snapshot of all queryable properties (keys and values), you can call
    "Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" without parameters (or with a NoneType or a blank property key). Using specific keys to query individual properties will
    be faster. Note that getting a property using an invalid key will return a trivial result.

    Setting values:
    Invoke "Project:SetSetting", "Timeline:SetSetting" or "MediaPoolItem:SetClipProperty" with the appropriate property key and a valid value. When setting a parameter, please check the return value to
    ensure the success of the operation. You can troubleshoot the validity of keys and values by setting the desired result from the UI and checking property snapshots before and after the change.

    The following Project properties have specifically enumerated values:
    "superScale" - the property value is an enumerated integer between 0 and 4 with these meanings: 0=Auto, 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.
                   for super scale multiplier '2x Enhanced', exactly 4 arguments must be passed as outlined below. If less than 4 arguments are passed, it will default to 2x.
    Affects:
    • x = Project:GetSetting('superScale') and Project:SetSetting('superScale', x)
    • for '2x Enhanced' --> Project:SetSetting('superScale', 2, sharpnessValue, noiseReductionValue), where sharpnessValue is a float in the range [0.0, 1.0] and noiseReductionValue is a float in the range [0.0, 1.0]

    "timelineFrameRate" - the property value is one of the frame rates available to the user in project settings under "Timeline frame rate" option. Drop Frame can be configured for supported frame rates
                          by appending the frame rate with "DF", e.g. "29.97 DF" will enable drop frame and "29.97" will disable drop frame
    Affects:
    • x = Project:GetSetting('timelineFrameRate') and Project:SetSetting('timelineFrameRate', x)

    The following Clip properties have specifically enumerated values:
    "Super Scale" - the property value is an enumerated integer between 1 and 4 with these meanings: 1=no scaling, and 2, 3 and 4 represent the Super Scale multipliers 2x, 3x and 4x.
                    for super scale multiplier '2x Enhanced', exactly 4 arguments must be passed as outlined below. If less than 4 arguments are passed, it will default to 2x.
    Affects:
    • x = MediaPoolItem:GetClipProperty('Super Scale') and MediaPoolItem:SetClipProperty('Super Scale', x)
    • for '2x Enhanced' --> MediaPoolItem:SetClipProperty('Super Scale', 2, sharpnessValue, noiseReductionValue), where sharpnessValue is a float in the range [0.0, 1.0] and noiseReductionValue is a float in the range [0.0, 1.0]

    "Cloud Sync" = the property value is an enumerated integer that will correspond to one of the following enums:
    * resolve.CLOUD_SYNC_DEFAULT                == -1
    * resolve.CLOUD_SYNC_DOWNLOAD_IN_QUEUE      == 0
    * resolve.CLOUD_SYNC_DOWNLOAD_IN_PROGRESS   == 1
    * resolve.CLOUD_SYNC_DOWNLOAD_SUCCESS       == 2
    * resolve.CLOUD_SYNC_DOWNLOAD_FAIL          == 3
    * resolve.CLOUD_SYNC_DOWNLOAD_NOT_FOUND     == 4

    * resolve.CLOUD_SYNC_UPLOAD_IN_QUEUE        == 5
    * resolve.CLOUD_SYNC_UPLOAD_IN_PROGRESS     == 6
    * resolve.CLOUD_SYNC_UPLOAD_SUCCESS         == 7
    * resolve.CLOUD_SYNC_UPLOAD_FAIL            == 8
    * resolve.CLOUD_SYNC_UPLOAD_NOT_FOUND       == 9

    * resolve.CLOUD_SYNC_SUCCESS                == 10

    Audio Mapping
    ---------------
    This section covers the output for mpItem.GetAudioMapping() and timelineItem.GetSourceAudioChannelMapping()
    Mapping format (json result) is similar for mpItem and timelineItem.

    This section will follow an example of an mpItem that has audio from its embedded source, and from two other clips that are linked to it.
    The audio clip attributes of this mpItem will show 3 tracks.

    Assume that (A) the embedded track is of format/type 'stereo' (2 channels),
                (B) linked clip 1 track is of format/type '7.1' (8 channels),
                (C) linked clip 2 track is '5.1' (6 channels)
    and assume that the format/type was not changed further.

    mpItem.GetAudioMapping() returns a string of the form:
        {
          "embedded_audio_channels": 2,                 # Total number of embedded channels across all tracks
          "linked_audio": {                             # A list of only linked audio information
            "1": {                                      # Same as (B) above
              "channels": 8,
              "path": FILE_PATH
            },
            "2": {                                      # Same as (C) above
              "channels": 6,
              "path": FILE_PATH
            }
          },
          "track_mapping": {                            # Listing of all the tracks. Output here will match what is seen in the audio clip attributes menu on the UI.
            "1": {
              "channel_idx": [1, 3],                    # In this case, channel index '1' corresponds to first channel of (A), channel index '3' will correspond to the first channel of (B)
              "mute": true,                             # Mute 'true' indicates track is muted. Valid value is true/false.
              "type": "Stereo"                          # The length of the 'channel_idx' list will always correspond to the number of channels the format specified in 'type' will allow.
                                                        # In this case, 'Stereo' allows 2 channels and so the length of the 'channel_idx' list is 2.
            },
            "2": {
              "channel_idx": [3, 4, 5, 6, 7, 8, 9, 10], # Channel indices here are following the default for (B)
              "mute": true,
              "type": "7.1"
            },
            "3": {
              "channel_idx": [1, 1, 1, 1, 15, 16],      # The first four channels for this track correspond to the first channel of (A), and the final 2 follow the default for (C)
              "mute": false,
              "type": "5.1"
            }
          }
        }


    Auto Caption Settings
    ----------------------
    This section covers the supported settings for the method Timeline.CreateSubtitlesFromAudio({autoCaptionSettings})

    The parameter setting is a dictionary containing the following keys:
    * resolve.SUBTITLE_LANGUAGE: languageID (see below), [resolve.AUTO_CAPTION_AUTO by default]
    * resolve.SUBTITLE_CAPTION_PRESET: presetType (see below), [resolve.AUTO_CAPTION_SUBTITLE_DEFAULT by default]
    * resolve.SUBTITLE_CHARS_PER_LINE: Number between 1 and 60 inclusive [42 by default]
    * resolve.SUBTITLE_LINE_BREAK: lineBreakType (see below), [resolve.AUTO_CAPTION_LINE_SINGLE by default]
    * resolve.SUBTITLE_GAP: Number between 0 and 10 inclusive [0 by default]

    Note that the default values for some keys may change based on values defined for other keys, as per the UI.
    For example, if the following dictionary is supplied,
        CreateSubtitlesFromAudio( { resolve.SUBTITLE_LANGUAGE = resolve.AUTO_CAPTION_KOREAN,
                                    resolve.SUBTITLE_CAPTION_PRESET = resolve.AUTO_CAPTION_NETFLIX } )
    the default value for resolve.SUBTITLE_CHARS_PER_LINE will be 16 instead of 42

    languageIDs:
    * resolve.AUTO_CAPTION_AUTO
    * resolve.AUTO_CAPTION_DANISH
    * resolve.AUTO_CAPTION_DUTCH
    * resolve.AUTO_CAPTION_ENGLISH
    * resolve.AUTO_CAPTION_FRENCH
    * resolve.AUTO_CAPTION_GERMAN
    * resolve.AUTO_CAPTION_ITALIAN
    * resolve.AUTO_CAPTION_JAPANESE
    * resolve.AUTO_CAPTION_KOREAN
    * resolve.AUTO_CAPTION_MANDARIN_SIMPLIFIED
    * resolve.AUTO_CAPTION_MANDARIN_TRADITIONAL
    * resolve.AUTO_CAPTION_NORWEGIAN
    * resolve.AUTO_CAPTION_PORTUGUESE
    * resolve.AUTO_CAPTION_RUSSIAN
    * resolve.AUTO_CAPTION_SPANISH
    * resolve.AUTO_CAPTION_SWEDISH

    presetTypes:
    * resolve.AUTO_CAPTION_SUBTITLE_DEFAULT
    * resolve.AUTO_CAPTION_TELETEXT
    * resolve.AUTO_CAPTION_NETFLIX

    lineBreakTypes:
    * resolve.AUTO_CAPTION_LINE_SINGLE
    * resolve.AUTO_CAPTION_LINE_DOUBLE


    Looking up Render Settings
    --------------------------
    This section covers the supported settings for the method SetRenderSettings({settings})

    The parameter setting is a dictionary containing the following keys:
        - "SelectAllFrames": Bool (when set True, the settings MarkIn and MarkOut are ignored)
        - "MarkIn": int
        - "MarkOut": int
        - "TargetDir": string
        - "CustomName": string
        - "UniqueFilenameStyle": 0 - Prefix, 1 - Suffix.
        - "ExportVideo": Bool
        - "ExportAudio": Bool
        - "FormatWidth": int
        - "FormatHeight": int
        - "FrameRate": float (examples: 23.976, 24)
        - "PixelAspectRatio": string (for SD resolution: "16_9" or "4_3") (other resolutions: "square" or "cinemascope")
        - "VideoQuality" possible values for current codec (if applicable):
        -    0 (int) - will set quality to automatic
        -    [1 -> MAX] (int) - will set input bit rate
        -    ["Least", "Low", "Medium", "High", "Best"] (String) - will set input quality level
        - "AudioCodec": string (example: "aac")
        - "AudioBitDepth": int
        - "AudioSampleRate": int
        - "ColorSpaceTag" : string (example: "Same as Project", "AstroDesign")
        - "GammaTag" : string (example: "Same as Project", "ACEScct")
        - "ExportAlpha": Bool
        - "EncodingProfile": string (example: "Main10"). Can only be set for H.264 and H.265.
        - "MultiPassEncode": Bool. Can only be set for H.264.
        - "AlphaMode": 0 - Premultiplied, 1 - Straight. Can only be set if "ExportAlpha" is true.
        - "NetworkOptimization": Bool. Only supported by QuickTime and MP4 formats.

    Looking up timeline export properties
    -------------------------------------
    This section covers the parameters for the argument Export(fileName, exportType, exportSubtype).

    exportType can be one of the following constants:
        - resolve.EXPORT_AAF
        - resolve.EXPORT_DRT
        - resolve.EXPORT_EDL
        - resolve.EXPORT_FCP_7_XML
        - resolve.EXPORT_FCPXML_1_8
        - resolve.EXPORT_FCPXML_1_9
        - resolve.EXPORT_FCPXML_1_10
        - resolve.EXPORT_HDR_10_PROFILE_A
        - resolve.EXPORT_HDR_10_PROFILE_B
        - resolve.EXPORT_TEXT_CSV
        - resolve.EXPORT_TEXT_TAB
        - resolve.EXPORT_DOLBY_VISION_VER_2_9
        - resolve.EXPORT_DOLBY_VISION_VER_4_0
        - resolve.EXPORT_DOLBY_VISION_VER_5_1
        - resolve.EXPORT_OTIO
        - resolve.EXPORT_ALE
        - resolve.EXPORT_ALE_CDL
    exportSubtype can be one of the following enums:
        - resolve.EXPORT_NONE
        - resolve.EXPORT_AAF_NEW
        - resolve.EXPORT_AAF_EXISTING
        - resolve.EXPORT_CDL
        - resolve.EXPORT_SDL
        - resolve.EXPORT_MISSING_CLIPS
    Please note that exportSubType is a required parameter for resolve.EXPORT_AAF and resolve.EXPORT_EDL. For rest of the exportType, exportSubtype is ignored.
    When exportType is resolve.EXPORT_AAF, valid exportSubtype values are resolve.EXPORT_AAF_NEW and resolve.EXPORT_AAF_EXISTING.
    When exportType is resolve.EXPORT_EDL, valid exportSubtype values are resolve.EXPORT_CDL, resolve.EXPORT_SDL, resolve.EXPORT_MISSING_CLIPS and resolve.EXPORT_NONE.
    Note: Replace 'resolve.' when using the constants above, if a different Resolve class instance name is used.

    Unsupported exportType types
    ----------------------------
    Starting with DaVinci Resolve 18.1, the following export types are not supported:
        - resolve.EXPORT_FCPXML_1_3
        - resolve.EXPORT_FCPXML_1_4
        - resolve.EXPORT_FCPXML_1_5
        - resolve.EXPORT_FCPXML_1_6
        - resolve.EXPORT_FCPXML_1_7


    Looking up Timeline item properties
    -----------------------------------
    This section covers additional notes for the function "TimelineItem:SetProperty" and "TimelineItem:GetProperty". These functions are used to get and set properties mentioned.

    The supported keys with their accepted values are:
      "Pan" : floating point values from -4.0*width to 4.0*width
      "Tilt" : floating point values from -4.0*height to 4.0*height
      "ZoomX" : floating point values from 0.0 to 100.0
      "ZoomY" : floating point values from 0.0 to 100.0
      "ZoomGang" : a boolean value
      "RotationAngle" : floating point values from -360.0 to 360.0
      "AnchorPointX" : floating point values from -4.0*width to 4.0*width
      "AnchorPointY" : floating point values from -4.0*height to 4.0*height
      "Pitch" : floating point values from -1.5 to 1.5
      "Yaw" : floating point values from -1.5 to 1.5
      "FlipX" : boolean value for flipping horizontally
      "FlipY" : boolean value for flipping vertically
      "CropLeft" : floating point values from 0.0 to width
      "CropRight" : floating point values from 0.0 to width
      "CropTop" : floating point values from 0.0 to height
      "CropBottom" : floating point values from 0.0 to height
      "CropSoftness" : floating point values from -100.0 to 100.0
      "CropRetain" : boolean value for "Retain Image Position" checkbox
      "DynamicZoomEase" : A value from the following constants
         - DYNAMIC_ZOOM_EASE_LINEAR = 0
         - DYNAMIC_ZOOM_EASE_IN
         - DYNAMIC_ZOOM_EASE_OUT
         - DYNAMIC_ZOOM_EASE_IN_AND_OUT
      "CompositeMode" : A value from the following constants
         - COMPOSITE_NORMAL = 0
         - COMPOSITE_ADD
         - COMPOSITE_SUBTRACT
         - COMPOSITE_DIFF
         - COMPOSITE_MULTIPLY
         - COMPOSITE_SCREEN
         - COMPOSITE_OVERLAY
         - COMPOSITE_HARDLIGHT
         - COMPOSITE_SOFTLIGHT
         - COMPOSITE_DARKEN
         - COMPOSITE_LIGHTEN
         - COMPOSITE_COLOR_DODGE
         - COMPOSITE_COLOR_BURN
         - COMPOSITE_EXCLUSION
         - COMPOSITE_HUE
         - COMPOSITE_SATURATE
         - COMPOSITE_COLORIZE
         - COMPOSITE_LUMA_MASK
         - COMPOSITE_DIVIDE
         - COMPOSITE_LINEAR_DODGE
         - COMPOSITE_LINEAR_BURN
         - COMPOSITE_LINEAR_LIGHT
         - COMPOSITE_VIVID_LIGHT
         - COMPOSITE_PIN_LIGHT
         - COMPOSITE_HARD_MIX
         - COMPOSITE_LIGHTER_COLOR
         - COMPOSITE_DARKER_COLOR
         - COMPOSITE_FOREGROUND
         - COMPOSITE_ALPHA
         - COMPOSITE_INVERTED_ALPHA
         - COMPOSITE_LUM
         - COMPOSITE_INVERTED_LUM
      "Opacity" : floating point value from 0.0 to 100.0
      "Distortion" : floating point value from -1.0 to 1.0
      "RetimeProcess" : A value from the following constants
         - RETIME_USE_PROJECT = 0
         - RETIME_NEAREST
         - RETIME_FRAME_BLEND
         - RETIME_OPTICAL_FLOW
      "MotionEstimation" : A value from the following constants
         - MOTION_EST_USE_PROJECT = 0
         - MOTION_EST_STANDARD_FASTER
         - MOTION_EST_STANDARD_BETTER
         - MOTION_EST_ENHANCED_FASTER
         - MOTION_EST_ENHANCED_BETTER
         - MOTION_EST_SPEED_WARP_BETTER
         - MOTION_EST_SPEED_WARP_FASTER
      "Scaling" : A value from the following constants
         - SCALE_USE_PROJECT = 0
         - SCALE_CROP
         - SCALE_FIT
         - SCALE_FILL
         - SCALE_STRETCH
      "ResizeFilter" : A value from the following constants
         - RESIZE_FILTER_USE_PROJECT = 0
         - RESIZE_FILTER_SHARPER
         - RESIZE_FILTER_SMOOTHER
         - RESIZE_FILTER_BICUBIC
         - RESIZE_FILTER_BILINEAR
         - RESIZE_FILTER_BESSEL
         - RESIZE_FILTER_BOX
         - RESIZE_FILTER_CATMULL_ROM
         - RESIZE_FILTER_CUBIC
         - RESIZE_FILTER_GAUSSIAN
         - RESIZE_FILTER_LANCZOS
         - RESIZE_FILTER_MITCHELL
         - RESIZE_FILTER_NEAREST_NEIGHBOR
         - RESIZE_FILTER_QUADRATIC
         - RESIZE_FILTER_SINC
         - RESIZE_FILTER_LINEAR
    Values beyond the range will be clipped
    width and height are same as the UI max limits

    The arguments can be passed as a key and value pair or they can be grouped together into a dictionary (for python) or table (for lua) and passed
    as a single argument.

    Getting the values for the keys that uses constants will return the number which is in the constant

    ExportLUT notes
    ---------------
    The following section covers additional notes for TimelineItem.ExportLUT(exportType, path).

    Supported values for 'exportType' (enum) are:
        - resolve.EXPORT_LUT_17PTCUBE
        - resolve.EXPORT_LUT_33PTCUBE
        - resolve.EXPORT_LUT_65PTCUBE
        - resolve.EXPORT_LUT_PANASONICVLUT
    """

    AUTO_CAPTION_AUTO: Final
    AUTO_CAPTION_DANISH: Final
    AUTO_CAPTION_DUTCH: Final
    AUTO_CAPTION_ENGLISH: Final
    AUTO_CAPTION_FRENCH: Final
    AUTO_CAPTION_GERMAN: Final
    AUTO_CAPTION_ITALIAN: Final
    AUTO_CAPTION_JAPANESE: Final
    AUTO_CAPTION_KOREAN: Final
    AUTO_CAPTION_MANDARIN_SIMPLIFIED: Final
    AUTO_CAPTION_MANDARIN_TRADITIONAL: Final
    AUTO_CAPTION_NORWEGIAN: Final
    AUTO_CAPTION_PORTUGUESE: Final
    AUTO_CAPTION_RUSSIAN: Final
    AUTO_CAPTION_SPANISH: Final
    AUTO_CAPTION_SWEDISH: Final

    AUTO_CAPTION_SUBTITLE_DEFAULT: Final
    AUTO_CAPTION_TELETEXT: Final
    AUTO_CAPTION_NETFLIX: Final

    AUTO_CAPTION_LINE_SINGLE: Final
    AUTO_CAPTION_LINE_DOUBLE: Final

    KEYFRAME_MODE_ALL: 0
    KEYFRAME_MODE_COLOR: 1
    KEYFRAME_MODE_SIZING: 2

    CLOUD_SETTING_PROJECT_NAME: Final
    CLOUD_SETTING_PROJECT_MEDIA_PATH: Final
    CLOUD_SETTING_IS_COLLAB: Final
    CLOUD_SETTING_SYNC_MODE: Final
    CLOUD_SETTING_IS_CAMERA_ACCESS: Final

    CLOUD_SYNC_NONE: Final
    CLOUD_SYNC_PROXY_ONLY: Final
    CLOUD_SYNC_PROXY_AND_ORIG: Final

    CLOUD_SYNC_DEFAULT: -1
    CLOUD_SYNC_DOWNLOAD_IN_QUEUE: 0
    CLOUD_SYNC_DOWNLOAD_IN_PROGRESS: 1
    CLOUD_SYNC_DOWNLOAD_SUCCESS: 2
    CLOUD_SYNC_DOWNLOAD_FAIL: 3
    CLOUD_SYNC_DOWNLOAD_NOT_FOUND: 4

    CLOUD_SYNC_UPLOAD_IN_QUEUE: 5
    CLOUD_SYNC_UPLOAD_IN_PROGRESS: 6
    CLOUD_SYNC_UPLOAD_SUCCESS: 7
    CLOUD_SYNC_UPLOAD_FAIL: 8
    CLOUD_SYNC_UPLOAD_NOT_FOUND: 9

    CLOUD_SYNC_SUCCESS: 10

    DLB_BLEND_SHOTS: Final

    EXPORT_AAF: Final
    EXPORT_DRT: Final
    EXPORT_EDL: Final
    EXPORT_FCP_7_XML: Final
    EXPORT_FCPXML_1_8: Final
    EXPORT_FCPXML_1_9: Final
    EXPORT_FCPXML_1_10: Final
    EXPORT_HDR_10_PROFILE_A: Final
    EXPORT_HDR_10_PROFILE_B: Final
    EXPORT_TEXT_CSV: Final
    EXPORT_TEXT_TAB: Final
    EXPORT_DOLBY_VISION_VER_2_9: Final
    EXPORT_DOLBY_VISION_VER_4_0: Final
    EXPORT_DOLBY_VISION_VER_5_1: Final
    EXPORT_OTIO: Final

    EXPORT_NONE: Final
    EXPORT_AAF_NEW: Final
    EXPORT_AAF_EXISTING: Final
    EXPORT_CDL: Final
    EXPORT_SDL: Final
    EXPORT_MISSING_CLIPS: Final

    EXPORT_LUT_17PTCUBE: Final
    EXPORT_LUT_33PTCUBE: Final
    EXPORT_LUT_65PTCUBE: Final
    EXPORT_LUT_PANASONICVLUT: Final

    SUBTITLE_LANGUAGE: Final
    SUBTITLE_CAPTION_PRESET: Final
    SUBTITLE_CHARS_PER_LINE: Final
    SUBTITLE_LINE_BREAK: Final
    SUBTITLE_GAP: Final

    def Fusion(self) -> Fusion:
        """ Returns the Fusion object. Starting point for Fusion scripts. """
        ...

    def GetMediaStorage(self) -> MediaStorage:
        """ Returns the media storage object to query and act on media locations. """
        ...

    def GetProjectManager(self) -> ProjectManager:
        """ Returns the project manager object for currently open database. """
        ...

    def OpenPage(self, pageName: PageName) -> bool:
        """
        Switches to indicated page in DaVinci Resolve.
        Input can be one of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver").
        """
        ...

    def GetCurrentPage(self) -> PageName:
        """
        Returns the page currently displayed in the main window.
        Returned value can be one of ("media", "cut", "edit", "fusion", "color", "fairlight", "deliver", None).
        """
        ...

    def GetProductName(self) -> str:
        """ Returns product name. """
        ...

    def GetVersion(self) -> list:
        """ Returns list of product version fields in [major, minor, patch, build, suffix] format. """
        ...

    def GetVersionString(self) -> str:
        """ Returns product version in "major.minor.patch[suffix].build" format. """
        ...

    def LoadLayoutPreset(self, presetName: str) -> bool:
        """ Loads UI layout from saved preset named 'presetName'. """
        ...

    def UpdateLayoutPreset(self, presetName: str) -> bool:
        """ Overwrites preset named 'presetName' with current UI layout. """
        ...

    def ExportLayoutPreset(self, presetName: str, presetFilePath: str) -> bool:
        """ Exports preset named 'presetName' to path 'presetFilePath'. """
        ...

    def DeleteLayoutPreset(self, presetName: str) -> bool:
        """ Deletes preset named 'presetName'. """
        ...

    def SaveLayoutPreset(self, presetName: str) -> bool:
        """ Saves current UI layout as a preset named 'presetName'. """
        ...

    def ImportLayoutPreset(self, presetFilePath: str, presetName: Optional[str]) -> bool:
        """
        Imports preset from path 'presetFilePath'.
        The optional argument 'presetName' specifies how the preset shall be named. If not specified, the preset is named based on the filename.
        """
        ...

    def Quit(self) -> None:
        """ Quits the Resolve App. """
        ...

    def ImportRenderPreset(self, presetPath: str) -> bool:
        """ Import a preset from presetPath (string) and set it as current preset for rendering. """
        ...

    def ExportRenderPreset(self, presetName: str, exportPath: str) -> bool:
        """ Export a preset to a given path (string) if presetName(string) exists. """
        ...

    def ImportBurnInPreset(self, presetPath: str) -> bool:
        """ Import a data burn in preset from a given presetPath (string) """
        ...

    def ExportBurnInPreset(self, presetName: str, exportPath: str) -> bool:
        """ Export a data burn in preset to a given path (string) if presetName (string) exists. """
        ...

    def GetKeyframeMode(self) -> KeyframeMode:
        """
        Returns the currently set keyframe mode (int).
        Refer to section 'Keyframe Mode information' below for details.
        """
        ...

    def SetKeyframeMode(self, keyframeMode: KeyframeMode) -> bool:
        """
        Returns True when 'keyframeMode'(enum) is successfully set.
        Refer to section 'Keyframe Mode information' below for details.
        """
        ...


class ProjectManager:

    def ArchiveProject(self, projectName: str, filePath: str, isArchiveSrcMedia: bool = True, isArchiveRenderCache: bool = True, isArchiveProxyMedia: bool = False) -> bool:
        """ Archives project to provided file path with the configuration as provided by the optional arguments"""
        ...

    def CreateProject(self, projectName: str) -> Project | None:
        """ Creates and returns a project if projectName (string) is unique, and None if it is not. """
        ...

    def DeleteProject(self, projectName: str) -> bool:
        """ Delete project in the current folder if not currently loaded """
        ...

    def LoadProject(self, projectName: str) -> Project | None:
        """ Loads and returns the project with name = projectName (string) if there is a match found, and None if there is no matching Project. """
        ...

    def GetCurrentProject(self) -> Project:
        """ Returns the currently loaded Resolve project. """
        ...

    def SaveProject(self) -> bool:
        """ Saves the currently loaded project with its own name. Returns True if successful. """
        ...

    def CloseProject(self, project: Project) -> bool:
        """ Closes the specified project without saving. """
        ...

    def CreateFolder(self, folderName: str) -> bool:
        """ Creates a folder if folderName (string) is unique. """
        ...

    def DeleteFolder(self, folderName: str) -> bool:
        """ Deletes the specified folder if it exists. Returns True in case of success. """
        ...

    def GetProjectListInCurrentFolder(self) -> List[str]:
        """ Returns a list of project names in current folder. """
        ...

    @deprecated
    def GetProjectsInCurrentFolder(self) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of project names in current folder.
        """
        ...

    def GetFolderListInCurrentFolder(self) -> List[str]:
        """ Returns a list of folder names in current folder. """
        ...

    @deprecated
    def GetFoldersInCurrentFolder(self) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of folder names in current folder.
        """
        ...

    def GotoRootFolder(self) -> bool:
        """ Opens root folder in database. """
        ...

    def GotoParentFolder(self) -> bool:
        """ Opens parent folder of current folder in database if current folder has parent. """
        ...

    def GetCurrentFolder(self) -> str:
        """ Returns the current folder name. """
        ...

    def OpenFolder(self, folderName: str) -> bool:
        """ Opens folder under given name. """
        ...

    def ImportProject(self, filePath: str, projectName: Optional[str]) -> bool:
        """ Imports a project from the file path provided with given project name, if any. Returns True if successful. """
        ...

    def ExportProject(self, projectName: str, filePath: str, withStillsAndLUTs: bool = True) -> bool:
        """ Exports project to provided file path, including stills and LUTs if withStillsAndLUTs is True (enabled by default). Returns True in case of success. """
        ...

    def RestoreProject(self, filePath: str, projectName: Optional[str]) -> bool:
        """ Restores a project from the file path provided with given project name, if any. Returns True if successful. """
        ...

    def GetCurrentDatabase(self) -> DbInfo:
        """ Returns a dictionary (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to the current database connection """
        ...

    def GetDatabaseList(self) -> List[DbInfo]:
        """ Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to all the databases added to Resolve """
        ...

    def SetCurrentDatabase(self, dbInfo: DbInfo) -> bool:
        """ Switches current database connection to the database specified by the keys below, and closes any open project. """
        ...

    def CreateCloudProject(self, cloudSettings: CloudProjectsSettings) -> Project:
        """
        Creates and returns a cloud project.
        '{cloudSettings}': Check 'Cloud Projects Settings' subsection below for more information.
        """
        ...

    def ImportCloudProject(self, filePath: str, cloudSettings: CloudProjectsSettings) -> bool:
        """
        Returns True if import cloud project is successful; False otherwise
        'filePath': String; filePath of file to import
        '{cloudSettings}': Check 'Cloud Projects Settings' subsection below for more information.
        """
        ...

    def RestoreCloudProject(self, folderPath: str, cloudSettings: CloudProjectsSettings) -> bool:
        """
        Returns True if restore cloud project is successful; False otherwise
        'folderPath': String; path of folder to restore
        '{cloudSettings}': Check 'Cloud Projects Settings' subsection below for more information.
        """
        ...


class Project:

    def GetMediaPool(self) -> MediaPool:
        """ Returns the Media Pool object. """
        ...

    def GetTimelineCount(self) -> int:
        """ Returns the number of timelines currently present in the project. """
        ...

    def GetTimelineByIndex(self, idx: int) -> Timeline:
        """ Returns timeline at the given index, 1 <= idx <= project.GetTimelineCount() """
        ...

    def GetCurrentTimeline(self) -> Timeline:
        """ Returns the currently loaded timeline. """
        ...

    def SetCurrentTimeline(self, timeline: Timeline) -> bool:
        """ Sets given timeline as current timeline for the project. Returns True if successful. """
        ...

    def GetGallery(self) -> Gallery:
        """ Returns the Gallery object. """
        ...

    def GetName(self) -> str:
        """ Returns project name. """
        ...

    def SetName(self, projectName: str) -> bool:
        """ Sets project name if given projectName (string) is unique. """
        ...

    def GetPresetList(self) -> List[Preset]:
        """ Returns a list of presets and their information. """
        ...

    @deprecated
    def GetPresets(self) -> dict[Any, Preset]:
        """
        Deprecated!

        Returns a dict of presets and their information.
        """
        ...

    def SetPreset(self, presetName: str) -> bool:
        """ Sets preset by given presetName (string) into project. """
        ...

    def AddRenderJob(self) -> str:
        """
        Adds a render job based on current render settings to the render queue.
        Returns a unique job id (string) for the new render job.
        """
        ...

    def DeleteRenderJob(self, jobId: str) -> bool:
        """ Deletes render job for input job id (string). """
        ...

    @deprecated
    def DeleteRenderJobByIndex(self, idx: int) -> bool:
        """
        No longer supported!
        
        Please use unique job ids (string) instead of indices.
        """
        ...

    def DeleteAllRenderJobs(self) -> bool:
        """ Deletes all render jobs in the queue. """
        ...

    def GetRenderJobList(self) -> List[RenderJob]:
        """ Returns a list of render jobs and their information. """
        ...

    @deprecated
    def GetRenderJobs(self) -> dict[Any, RenderJob]:
        """
        Deprecated!

        Returns a dict of render jobs and their information.
        """
        ...

    def GetRenderPresetList(self) -> List[RenderPreset]:
        """ Returns a list of render presets and their information. """
        ...

    @deprecated
    def GetRenderPresets(self) -> dict[Any, RenderPreset]:
        """
        Deprecated!

        Returns a dict of render presets and their information.
        """
        ...

    @overload
    def StartRendering(self, jobId1: str, *args: str) -> bool:
        """ Starts rendering jobs indicated by the input job ids. """
        ...

    @overload
    def StartRendering(self, jobIds: List[str], isInteractiveMode: bool = False) -> bool:
        """
        Starts rendering jobs indicated by the input job ids.
        The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.
        """
        ...

    @overload
    def StartRendering(self, isInteractiveMode: bool = False) -> bool:
        """
        Starts rendering all queued render jobs.
        The optional "isInteractiveMode", when set, enables error feedback in the UI during rendering.
        """
        ...

    @deprecated
    @overload
    def StartRendering(self, index1: int, *args: int) -> bool:
        """
        No longer supported!

        Please use unique job ids (string) instead of indices.
        """
        ...

    @deprecated
    @overload
    def StartRendering(self, idxs: List[int]) -> bool:
        """
        No longer supported!

        Please use unique job ids (string) instead of indices.
        """
        ...

    def StopRendering(self) -> None:
        """ Stops any current render processes. """
        ...

    def IsRenderingInProgress(self) -> bool:
        """ Returns True if rendering is in progress. """
        ...

    def LoadRenderPreset(self, presetName: str) -> bool:
        """ Sets a preset as current preset for rendering if presetName (string) exists. """
        ...

    def SaveAsNewRenderPreset(self, presetName: str) -> bool:
        """ Creates new render preset by given name if presetName(string) is unique. """
        ...

    def SetRenderSettings(self, settings: RenderSettings) -> bool:
        """
        Sets given settings for rendering. Settings is a dict, with support for the keys:
        Refer to "Looking up render settings" section for information for supported settings
        """
        ...

    @overload
    def GetRenderJobStatus(self, jobId: str) -> RenderJobStatus:
        """ Returns a dict with job status and completion percentage of the job by given jobId (string). """
        ...

    @deprecated
    @overload
    def GetRenderJobStatus(self, idx: int) -> RenderJobStatus:
        """ Returns a dict with job status and completion percentage of the job by given jobId (string). """
        ...

    def GetSetting(self, settingName: str) -> str:
        """
        Returns value of project setting (indicated by settingName, string).

        Note:
            - settingName videoMonitorUseRec601For422SDI is now replaced with videoMonitorUseMatrixOverrideFor422SDI and videoMonitorMatrixOverrideFor422SDI.
            - settingName perfProxyMediaOn is now replaced with perfProxyMediaMode which takes values 0 - disabled, 1 - when available, 2 - when source not available.
        """
        ...

    def SetSetting(self, settingName: str, settingValue: str) -> bool:
        """
        Sets the project setting (indicated by settingName, string) to the value (settingValue, string).

        Note: see `GetSetting` method for a list of obsolete setting names.
        """
        ...

    def GetRenderFormats(self) -> dict[str, str]:
        """ Returns a dict (format -> file extension) of available render formats. """
        ...

    def GetRenderCodecs(self, renderFormat: str) -> dict[str, str]:
        """ Returns a dict (codec description -> codec name) of available codecs for given render format (string). """
        ...

    def GetCurrentRenderFormatAndCodec(self) -> RenderFormatAndCodec:
        """ Returns a dict with currently selected format 'format' and render codec 'codec'. """
        ...

    def SetCurrentRenderFormatAndCodec(self, format: str, codec: str) -> bool:
        """ Sets given render format (string) and render codec (string) as options for rendering. """
        ...

    def GetCurrentRenderMode(self) -> RenderMode:
        """ Returns the render mode: 0 - Individual clips, 1 - Single clip. """
        ...

    def SetCurrentRenderMode(self, renderMode: RenderMode) -> bool:
        """ Sets the render mode. Specify renderMode = 0 for Individual clips, 1 for Single clip. """
        ...

    def GetRenderResolutions(self, format: Optional[str], codec: Optional[str]) -> List[RenderResolution]:
        """
        Returns list of resolutions applicable for the given render format (string) and render codec (string).
        Returns full list of resolutions if no argument is provided.
        Each element in the list is a dictionary with 2 keys "Width" and "Height".
        """
        ...

    def RefreshLUTList(self) -> bool:
        """ Refreshes LUT List """
        ...

    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the project item """
        ...

    def InsertAudioToCurrentTrackAtPlayhead(self, mediaPath: str, startOffsetInSamples: int, durationInSamples: int) -> bool:
        """
        Inserts the media specified by mediaPath (string) with startOffsetInSamples (int) and durationInSamples (int) at the playhead on a selected track on the Fairlight page.
        Returns True if successful, otherwise False.
        """
        ...

    def LoadBurnInPreset(self, presetName: str) -> bool:
        """ Loads user defined data burn in preset for project when supplied presetName (string). Returns true if successful. """
        ...

    def ExportCurrentFrameAsStill(self, filePath: str) -> bool:
        """
        Exports current frame as still to supplied filePath. filePath must end in valid export file format.
        Returns True if succssful, False otherwise.
        """

    def GetColorGroupsList(self) -> List[ColorGroup]:
        """ Returns a list of all group objects in the timeline. """
        ...

    def AddColorGroup(self, groupName: str) -> ColorGroup:
        """ Creates a new ColorGroup. groupName must be a unique string. """
        ...

    def DeleteColorGroup(self, colorGroup: ColorGroup) -> bool:
        """ Deletes the given color group and sets clips to ungrouped. """
        ...


class MediaStorage:

    def GetMountedVolumeList(self) -> List[str]:
        """ Returns list of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage. """
        ...

    @deprecated
    def GetMountedVolumes(self) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of folder paths corresponding to mounted volumes displayed in Resolve’s Media Storage.
        """
        ...

    def GetSubFolderList(self, folderPath: str) -> List[str]:
        """ Returns list of folder paths in the given absolute folder path. """
        ...

    @deprecated
    def GetSubFolders(self, folderPath: str) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of folder paths in the given absolute folder path.
        """
        ...

    def GetFileList(self, folderPath: str) -> List[str]:
        """
        Returns list of media and file listings in the given absolute folder path.
        Note that media listings may be logically consolidated entries.
        """
        ...

    @deprecated
    def GetFiles(self, folderPath: str) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of media and file listings in the given absolute folder path.
        Note that media listings may be logically consolidated entries.
        """
        ...

    def RevealInStorage(self, path: str) -> bool:
        """ Expands and displays given file/folder path in Resolve’s Media Storage. """
        ...

    @overload
    def AddItemListToMediaPool(self, item1: str, *args: str) -> List[MediaPoolItem]:
        """
        Adds specified file/folder paths from Media Storage into current Media Pool folder.
        Input is one or more file/folder paths.
        Returns a list of the MediaPoolItems created.
        """
        ...

    @overload
    def AddItemListToMediaPool(self, items: List[str]) -> List[MediaPoolItem]:
        """
        Adds specified file/folder paths from Media Storage into current Media Pool folder.
        Input is an array of file/folder paths.
        Returns a list of the MediaPoolItems created.
        """
        ...

    @overload
    def AddItemListToMediaPool(self, itemInfo: List[MediaPoolItemInfo]) -> List[MediaPoolItem]:
        """
        Adds list of itemInfos specified as dict of "media", "startFrame" (int), "endFrame" (int)
        from Media Storage into current Media Pool folder. Returns a list of the MediaPoolItems created.
        """
        ...

    @deprecated
    def AddItemsToMediaPool(self, item1: str, *args: str) -> dict[Any, MediaPoolItem]:
        """
        Deprecated!

        Adds specified file/folder paths from Media Storage into current Media Pool folder.
        Input is one or more file/folder paths. Returns a dict of the MediaPoolItems created.
        """
        ...

    @deprecated
    def AddItemsToMediaPool(self, items: List[str]) -> dict[Any, MediaPoolItem]:
        """
        Deprecated!

        Adds specified file/folder paths from Media Storage into current Media Pool folder.
        Input is an array of file/folder paths. Returns a dict of the MediaPoolItems created.
        """
        ...

    def AddClipMattesToMediaPool(self, mediaPoolItem: MediaPoolItem, paths: List[str], stereoEye: Optional[StereoEye]) -> bool:
        """
        Adds specified media files as mattes for the specified MediaPoolItem.
        StereoEye is an optional argument for specifying which eye to add the matte to for stereo clips ("left" or "right").
        Returns True if successful.
        """
        ...

    def AddTimelineMattesToMediaPool(self, paths: List[str]) -> List[MediaPoolItem]:
        """
        Adds specified media files as timeline mattes in current media pool folder.
        Returns a list of created MediaPoolItems.
        """
        ...


class MediaPool:
    
    def GetRootFolder(self) -> Folder:
        """ Returns root Folder of Media Pool """
        ...

    def AddSubFolder(self, folder: Folder, name: str) -> Folder:
        """ Adds new subfolder under specified Folder object with the given name. """
        ...
    
    def RefreshFolders(self) -> bool:
        """ Updates the folders in collaboration mode """
        ...
    
    def CreateEmptyTimeline(self, name: str) -> Timeline:
        """ Adds new timeline with given name. """
        ...
    
    def AppendToTimeline(self, clip1: MediaPoolItem, *args: MediaPoolItem) -> List[TimelineItem]:
        """ Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems. """
        ...

    @overload
    def AppendToTimeline(self, clips: List[MediaPoolItem]) -> List[TimelineItem]:
        """ Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems. """
        ...

    @overload
    def AppendToTimeline(self, clipInfo: List[MediaPoolClipInfo]) -> [TimelineItem]:
        """
        Appends list of clipInfos specified as dict of "mediaPoolItem", "startFrame" (float/int), "endFrame" (float/int),
        (optional) "mediaType" (int; 1 - Video only, 2 - Audio only), "trackIndex" (int) and "recordFrame" (float/int).
        Returns the list of appended timelineItems.
        """
        ...

    @overload
    def CreateTimelineFromClips(self, name: str, clip1: MediaPoolItem, *args: MediaPoolItem) -> Timeline:
        """ Creates new timeline with specified name, and appends the specified MediaPoolItem objects. """
        ...

    @overload
    def CreateTimelineFromClips(self, name: str, clips: List[MediaPoolItem]) -> Timeline:
        """ Creates new timeline with specified name, and appends the specified MediaPoolItem objects. """
        ...

    @overload
    def CreateTimelineFromClips(self, name: str, clipInfo: List[MediaPoolClipInfo]) -> Timeline:
        """ Creates new timeline with specified name, appending the list of clipInfos specified as a dict of "mediaPoolItem", "startFrame" (float/int), "endFrame" (float/int), "recordFrame" (float/int). """
        ...

    def ImportTimelineFromFile(self, filePath: str, importOptions: TimelineImportOptions) -> Timeline:
        """
        Creates timeline based on parameters within given file (AAF/EDL/XML/FCPXML/DRT/ADL/OTIO) and optional importOptions dict, with support for the keys:
        "timelineName": string, specifies the name of the timeline to be created. Not valid for DRT import
        "importSourceClips": Bool, specifies whether source clips should be imported, True by default. Not valid for DRT import
        "sourceClipsPath": string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if "importSourceClips" is True
        "sourceClipsFolders": List of Media Pool folder objects to search for source clips if the media is not present in current folder and if "importSourceClips" is False. Not valid for DRT import
        "interlaceProcessing": Bool, specifies whether to enable interlace processing on the imported timeline being created. valid only for AAF import
        """
        ...
    
    def DeleteTimelines(self, timeline: List[Timeline]) -> bool:
        """ Deletes specified timelines in the media pool. """
        ...
    
    def GetCurrentFolder(self) -> Folder:
        """ Returns currently selected Folder. """
        ...
    
    def SetCurrentFolder(self, folder: Folder) -> bool:
        """ Sets current folder by given Folder. """
        ...
    
    def DeleteClips(self, clips: List[MediaPoolItem]) -> bool:
        """ Deletes specified clips or timeline mattes in the media pool """
        ...

    def ImportFolderFromFile(self, filePath: str, sourceClipsPath: str = '') -> bool:
        """
        Returns true if import from given DRB filePath is successful, false otherwise
        sourceClipsPath is a string that specifies a filesystem path to search for source clips if the media is inaccessible in their original path, empty by default
        """
        ...
    
    def DeleteFolders(self, subfolders: List[Folder]) -> bool:
        """ Deletes specified subfolders in the media pool """
        ...
    
    def MoveClips(self, clips: List[MediaPoolItem], targetFolder: Folder) -> bool:
        """ Moves specified clips to target folder. """
        ...
    
    def MoveFolders(self, folders: List[Folder], targetFolder: Folder) -> bool:
        """ Moves specified folders to target folder. """
        ...
    
    def GetClipMatteList(self, mediaPoolItem: MediaPoolItem) -> List[str]:
        """ Get mattes for specified MediaPoolItem, as a list of paths to the matte files. """
        ...
    
    def GetTimelineMatteList(self, folder: Folder) -> List[MediaPoolItem]:
        """ Get mattes in specified Folder, as list of MediaPoolItems. """
        ...
    
    def DeleteClipMattes(self, mediaPoolItem: MediaPoolItem, paths: List[str]) -> bool:
        """ Delete mattes based on their file paths, for specified MediaPoolItem. Returns True on success. """
        ...
    
    def RelinkClips(self, mediaPoolItem: List[MediaPoolItem], folderPath: str) -> bool:
        """ Update the folder location of specified media pool clips with the specified folder path. """
        ...
    
    def UnlinkClips(self, mediaPoolItem: List[MediaPoolItem]) -> bool:
        """ Unlink specified media pool clips. """
        ...

    @overload
    def ImportMedia(self, items: List[str]) -> List[MediaPoolItem]:
        """
        Imports specified file/folder paths into current Media Pool folder. Input is an array of file/folder paths.
        Returns a list of the MediaPoolItems created.
        """
        ...

    @overload
    def ImportMedia(self, clipInfo: List[ImportClipInfo]) -> List[MediaPoolItem]:
        """
        Imports file path(s) into current Media Pool folder as specified in list of clipInfo dict. Returns a list of the MediaPoolItems created.
        Each clipInfo gets imported as one MediaPoolItem unless 'Show Individual Frames' is turned on.
        Example: ImportMedia([{"FilePath":"file_%03d.dpx", "StartIndex":1, "EndIndex":100}]) would import clip "file_[001-100].dpx".
        """
        ...
    
    def ExportMetadata(self, fileName: str, clips: List[MediaPoolItem]) -> bool:
        """
        Exports metadata of specified clips to 'fileName' in CSV format.
        If no clips are specified, all clips from media pool will be used.
        """
        ...
    
    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the media pool """
        ...

    def CreateStereoClip(self, LeftMediaPoolItem: MediaPoolItem, RightMediaPoolItem: MediaPoolItem) -> MediaPoolItem:
        """ Takes in two existing media pool items and creates a new 3D stereoscopic media pool entry replacing the input media in the media pool. """
        ...

    def GetSelectedClips(self) -> List[MediaPoolItem]:
        """ Returns the current selected MediaPoolItems """
        ...

    def SetSelectedClip(self, mediaPoolItem: MediaPoolItem) -> bool:
        """ Sets the selected MediaPoolItem to the given MediaPoolItem """
        ...


class Folder:

    def GetClipList(self) -> List[MediaPoolItem]:
        """ Returns a list of clips (items) within the folder. """
        ...

    @deprecated
    def GetClips(self) -> dict[Any, MediaPoolItem]:
        """
        Deprecated!

        Returns a dict of clips (items) within the folder.
        """

    def GetName(self) -> str:
        """ Returns the media folder name. """
        ...

    def GetSubFolderList(self) -> List[Folder]:
        """ Returns a list of subfolders in the folder. """
        ...

    @deprecated
    def GetSubFolders(self) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of subfolders in the folder.
        """

    def GetIsFolderStale(self) -> bool:
        """ Returns true if folder is stale in collaboration mode, false otherwise """
        ...

    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the media pool folder """
        ...

    def Export(self, filePath: str) -> bool:
        """ Returns true if export of DRB folder to filePath is successful, false otherwise """
        ...

    def TranscribeAudio(self) -> bool:
        """ Transcribes audio of the MediaPoolItems within the folder and nested folders. Returns True if successful; False otherwise """
        ...

    def ClearTranscription(self) -> bool:
        """ Clears audio transcription of the MediaPoolItems within the folder and nested folders. Returns True if successful; False otherwise. """
        ...


class MediaPoolItem:

    def GetName(self) -> str:
        """ Returns the clip name. """
        ...

    def GetMetadata(self, metadataType: Optional[str]) -> str | dict:
        """
        Returns the metadata value for the key 'metadataType'.
        If no argument is specified, a dict of all set metadata properties is returned.
        """
        ...

    @overload
    def SetMetadata(self, metadataType: str, metadataValue: str) -> bool:
        """ Sets the given metadata to metadataValue (string). Returns True if successful. """
        ...

    @overload
    def SetMetadata(self, metadata: dict[str, str]) -> bool:
        """ Sets the item metadata with specified 'metadata' dict. Returns True if successful. """
        ...

    def GetThirdPartyMetadata(self, metadataType: Optional[str] = None) -> str | dict:
        """
        Returns the third party metadata value for the key 'metadataType'.
        If no argument is specified, a dict of all set third parth metadata properties is returned.
        """
        ...

    @overload
    def SetThirdPartyMetadata(self, metadataType: str, metadataValue: str) -> bool:
        """ Sets/Add the given third party metadata to metadataValue (string). Returns True if successful. """
        ...

    @overload
    def SetThirdPartyMetadata(self, metadata: dict[str, str]) -> bool:
        """ Sets/Add the item third party metadata with specified 'metadata' dict. Returns True if successful. """
        ...

    def GetMediaId(self) -> str:
        """ Returns the unique ID for the MediaPoolItem. """
        ...

    def AddMarker(self, frameId: float, color: MarkerColor, name: str, note: str, duration: float, customData: Optional[str]) -> bool:
        """
        Creates a new marker at given frameId position and with given marker information.
        'customData' is optional and helps to attach user specific data to the marker.
        """
        ...

    def GetMarkers(self) -> dict[float, Marker]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their information.
        Example of output format: {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...}
        In the above example - there is one 'Green' marker at offset 96 (position of the marker)
        """
        ...

    def GetMarkerByCustomData(self, customData: str) -> dict[float, Marker]:
        """ Returns marker {information} for the first matching marker with specified customData. """
        ...

    def UpdateMarkerCustomData(self, frameId: float, customData: str) -> bool:
        """ Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers. """
        ...

    def GetMarkerCustomData(self, frameId: float) -> str:
        """ Returns customData string for the marker at given frameId position. """
        ...

    def DeleteMarkersByColor(self, color: MarkerColor | Literal['All']) -> bool:
        """ Delete all markers of the specified color from the media pool item. "All" as argument deletes all color markers. """
        ...

    def DeleteMarkerAtFrame(self, frameNum: float) -> bool:
        """ Delete marker at frame number from the media pool item. """
        ...

    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """ Delete first matching marker with specified customData. """
        ...

    def AddFlag(self, color: FlagColor) -> bool:
        """ Adds a flag with given color (string). """
        ...

    def GetFlagList(self) -> List[FlagColor]:
        """ Returns a list of flag colors assigned to the item. """
        ...

    @deprecated
    def GetFlags(self) -> dict[Any, FlagColor]:
        """
        Deprecated!

        Returns a dict of flag colors assigned to the item.
        """
        ...

    def ClearFlags(self, color: FlagColor | Literal['All']) -> bool:
        """ Clears the flag of the given color if one exists. An "All" argument is supported and clears all flags. """
        ...

    def GetClipColor(self) -> ClipColor:
        """ Returns the item color as a string. """
        ...

    def SetClipColor(self, colorName: ClipColor) -> bool:
        """ Sets the item color based on the colorName (string). """
        ...

    def ClearClipColor(self) -> bool:
        """ Clears the item color. """
        ...

    def GetClipProperty(self, propertyName: Optional[str]) -> str | dict:
        """
        Returns the property value for the key 'propertyName'.
        If no argument is specified, a dict of all clip properties is returned.
        """
        ...

    def SetClipProperty(self, propertyName: str, propertyValue: Any) -> bool:
        """ Sets the given property to propertyValue (string). """
        ...

    def LinkProxyMedia(self, proxyMediaFilePath: str) -> bool:
        """ Links proxy media located at path specified by arg 'proxyMediaFilePath' with the current clip. 'proxyMediaFilePath' should be absolute clip path. """
        ...

    def UnlinkProxyMedia(self) -> bool:
        """ Unlinks any proxy media associated with clip. """
        ...

    def ReplaceClip(self, filePath: str) -> bool:
        """ Replaces the underlying asset and metadata of MediaPoolItem with the specified absolute clip path. """
        ...

    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the media pool item """
        ...

    def TranscribeAudio(self) -> bool:
        """ Transcribes audio of the MediaPoolItem. Returns True if successful; False otherwise """
        ...

    def ClearTranscription(self) -> bool:
        """ Clears audio transcription of the MediaPoolItem. Returns True if successful; False otherwise. """
        ...

    def GetAudioMapping(self) -> str:
        """
        Returns a string with MediaPoolItem's audio mapping information.
        Check 'Audio Mapping' section below for more information.
        """
        ...


class Timeline:
    
    def GetName(self) -> str:
        """ Returns the timeline name. """
        ...

    def SetName(self, timelineName: str) -> bool:
        """ Sets the timeline name if timelineName (string) is unique. Returns True if successful. """
        ...
    
    def GetStartFrame(self) -> int:
        """ Returns the frame number at the start of timeline. """
        ...
    
    def GetEndFrame(self) -> int:
        """ Returns the frame number at the end of timeline. """
        ...
    
    def SetStartTimecode(self, timecode: str) -> bool:
        """ Set the start timecode of the timeline to the string 'timecode'. Returns true when the change is successful, false otherwise. """
        ...
    
    def GetStartTimecode(self) -> str:
        """ Returns the start timecode for the timeline. """
        ...
    
    def GetTrackCount(self, trackType: TrackType) -> int:
        """ Returns the number of tracks for the given track type ("audio", "video" or "subtitle"). """
        ...

    @overload
    def AddTrack(self, trackType: TrackType, subTrackType: SubTrackType) -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio"). Optional argument subTrackType is used for "audio" trackType.
        subTrackType can be one of {"mono", "stereo", "5.1", "5.1film", "7.1", "7.1film", "adaptive1", ... , "adaptive24"}
        """
        ...

    @overload
    def AddTrack(self, trackType: TrackType, newTrackOptions: NewTrackOptions) -> bool:
        """
        Adds track of trackType ("video", "subtitle", "audio").
        Optional newTrackOptions = {'audioType': same as subTrackType above, 'index': 1 <= index <= GetTrackCount(trackType))
        'audiotype' defaults to 'mono' if arg skipped and track type is ‘audio’.
        'index' if skipped (or if value not in bounds) appends track.
        """
        ...

    def DeleteTrack(self, trackType: TrackType, trackIndex: int) -> bool:
        """ Deletes track of trackType ("video", "subtitle", "audio") and given trackIndex. 1 <= trackIndex <= GetTrackCount(trackType). """
        ...

    def GetTrackSubType(self, trackType: TrackType, trackIndex: int) -> SubTrackType:
        """
        Returns an audio track's format.
        the return value is one of {"mono", "stereo", "5.1", "5.1film", "7.1", "7.1film", "adaptive1", ... , "adaptive24"} and matches the parameters 'subTrackType' and 'audioType' in timeline.AddTrack.
        returns a blank string for non audio tracks
        """
        ...

    def SetTrackEnable(self, trackType: TrackType, trackIndex: int, Bool: bool) -> bool:
        """
        Enables/Disables track with given trackType and trackIndex
        trackType is one of {"audio", "video", "subtitle"}
        1 <= trackIndex <= GetTrackCount(trackType).
        """
        ...

    def GetIsTrackEnabled(self, trackType: TrackType, trackIndex: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is enabled and False otherwise.
        trackType is one of {"audio", "video", "subtitle"}
        1 <= trackIndex <= GetTrackCount(trackType).
        """
        ...

    def SetTrackLock(self, trackType: TrackType, trackIndex: int, Bool: bool) -> bool:
        """
        Locks/Unlocks track with given trackType and trackIndex
        trackType is one of {"audio", "video", "subtitle"}
        1 <= trackIndex <= GetTrackCount(trackType).
        """
        ...

    def GetIsTrackLocked(self, trackType: TrackType, trackIndex: int) -> bool:
        """
        Returns True if track with given trackType and trackIndex is locked and False otherwise.
        trackType is one of {"audio", "video", "subtitle"}
        1 <= trackIndex <= GetTrackCount(trackType).
        """
        ...

    def DeleteClips(self, timelineItems: List[TimelineItem], Bool: bool) -> bool:
        """
        Deletes specified TimelineItems from the timeline, performing ripple delete if the second argument is True.
        Second argument is optional (The default for this is False)
        """

    def SetClipsLinked(self, timelineItems: List[TimelineItem], Bool: bool) -> bool:
        """ Links or unlinks the specified TimelineItems depending on second argument. """
        ...

    def GetItemListInTrack(self, trackType: TrackType, index: int) -> List[TimelineItem]:
        """ Returns a list of timeline items on that track (based on trackType and index). 1 <= index <= GetTrackCount(trackType). """
        ...

    @deprecated
    def GetItemsInTrack(self, trackType: TrackType, index: int) -> dict[Any, TimelineItem]:
        """
        Deprecated!

        Returns a dict of Timeline items on the video or audio track (based on trackType) at specified
        """

    def AddMarker(self, frameId: float, color: MarkerColor, name: str, note: str, duration: float, customData: Optional[str]) -> bool:
        """ Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker. """
        ...

    def GetMarkers(self) -> dict[float, Marker]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their information.
        Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at timeline offset 96
        """
        ...
    
    def GetMarkerByCustomData(self, customData: str) -> dict[float, Marker]:
        """ Returns marker {information} for the first matching marker with specified customData. """
        ...
    
    def UpdateMarkerCustomData(self, frameId: float, customData: str) -> bool:
        """ Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers. """
        ...
    
    def GetMarkerCustomData(self, frameId: float) -> str:
        """ Returns customData string for the marker at given frameId position. """
        ...
    
    def DeleteMarkersByColor(self, color: MarkerColor | Literal['All']) -> bool:
        """ Deletes all timeline markers of the specified color. An "All" argument is supported and deletes all timeline markers. """
        ...
    
    def DeleteMarkerAtFrame(self, frameNum: float) -> bool:
        """ Deletes the timeline marker at the given frame number. """
        ...
    
    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """ Delete first matching marker with specified customData. """
        ...
    
    @overload
    def ApplyGradeFromDRX(self, path: str, gradeMode: GradeMode, item1: TimelineItem, *args: TimelineItem) -> bool:
        """ Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned". """
        ...
    
    @overload
    def ApplyGradeFromDRX(self, path: str, gradeMode: GradeMode, items: List[TimelineItem]) -> bool:
        """ Loads a still from given file path (string) and applies grade to Timeline Items with gradeMode (int): 0 - "No keyframes", 1 - "Source Timecode aligned", 2 - "Start Frames aligned". """
        ...
    
    def GetCurrentTimecode(self) -> str:
        """ Returns a string timecode representation for the current playhead position, while on Cut, Edit, Color, Fairlight and Deliver pages. """
        ...
    
    def SetCurrentTimecode(self, timecode: str) -> bool:
        """ Sets current playhead position from input timecode for Cut, Edit, Color, Fairlight and Deliver pages. """
        ...
    
    def GetCurrentVideoItem(self) -> TimelineItem:
        """ Returns the current video timeline item. """
        ...
    
    def GetCurrentClipThumbnailImage(self) -> ThumbnailData:
        """
        Returns a dict (keys "width", "height", "format" and "data") with data containing raw thumbnail image data (RGB 8-bit image data encoded in base64 format) for current media in the Color Page.
        An example of how to retrieve and interpret thumbnails is provided in 6_get_current_media_thumbnail.py in the Examples folder.
        """
        ...
    
    def GetTrackName(self, trackType: TrackType, trackIndex: int) -> str:
        """ Returns the track name for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType). """
        ...

    def SetTrackName(self, trackType: TrackType, trackIndex: int, name: str) -> bool:
        """ Sets the track name (string) for track indicated by trackType ("audio", "video" or "subtitle") and index. 1 <= trackIndex <= GetTrackCount(trackType). """
        ...
    
    def DuplicateTimeline(self, timelineName: Optional[str]) -> Timeline:
        """ Duplicates the timeline and returns the created timeline, with the (optional) timelineName, on success. """
        ...

    def CreateCompoundClip(self, timelineItems: List[TimelineItem], clipInfo: Optional[TimelineClipInfo]) -> TimelineItem:
        """
        Creates a compound clip of input timeline items with an optional clipInfo map: {"startTimecode" : "00:00:00:00", "name" : "Compound Clip 1"}.
        It returns the created timeline item.
        """
        ...
    
    def CreateFusionClip(self, timelineItems: List[TimelineItem]) -> TimelineItem:
        """ Creates a Fusion clip of input timeline items. It returns the created timeline item. """
        ...
    
    def ImportIntoTimeline(self, filePath: str, importOptions: Optional[TimelineItemsImportOptions]) -> bool:
        """
        Imports timeline items from an AAF file and optional importOptions dict into the timeline, with support for the keys:
         - 'autoImportSourceClipsIntoMediaPool': Bool, specifies if source clips should be imported into media pool, True by default
         - 'ignoreFileExtensionsWhenMatching': Bool, specifies if file extensions should be ignored when matching, False by default
         - 'linkToSourceCameraFiles': Bool, specifies if link to source camera files should be enabled, False by default
         - 'useSizingInfo': Bool, specifies if sizing information should be used, False by default
         - 'importMultiChannelAudioTracksAsLinkedGroups': Bool, specifies if multi-channel audio tracks should be imported as linked groups, False by default
         - 'insertAdditionalTracks': Bool, specifies if additional tracks should be inserted, True by default
         - 'insertWithOffset': string, specifies insert with offset value in timecode format - defaults to "00:00:00:00", applicable if 'insertAdditionalTracks' is False
         - 'sourceClipsPath': string, specifies a filesystem path to search for source clips if the media is inaccessible in their original path and if 'ignoreFileExtensionsWhenMatching' is True
         - 'sourceClipsFolders': string, list of Media Pool folder objects to search for source clips if the media is not present in current folder
        """
        ...
    
    def Export(self, fileName: str, exportType: TimelineExportType, exportSubtype: TimelineExportSubtype) -> bool:
        """
        Exports timeline to 'fileName' as per input exportType & exportSubtype format.
        Refer to section "Looking up timeline export properties" for information on the parameters.
        """
        ...
    
    def GetSetting(self, settingName: str) -> str:
        """ Returns value of timeline setting (indicated by settingName : string). """
        ...
    
    def SetSetting(self, settingName: str, settingValue: str) -> bool:
        """ Sets timeline setting (indicated by settingName : string) to the value (settingValue : string). """
        ...
    
    def InsertGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """ Inserts a generator (indicated by generatorName : string) into the timeline. """
        ...
    
    def InsertFusionGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """ Inserts a Fusion generator (indicated by generatorName : string) into the timeline. """
        ...

    def InsertFusionCompositionIntoTimeline(self) -> TimelineItem:
        """ Inserts a Fusion composition into the timeline. """
        ...
    
    def InsertOFXGeneratorIntoTimeline(self, generatorName: str) -> TimelineItem:
        """ Inserts an OFX generator (indicated by generatorName : string) into the timeline. """
        ...

    def InsertTitleIntoTimeline(self, titleName: str) -> TimelineItem:
        """ Inserts a title (indicated by titleName : string) into the timeline. """
        ...

    def InsertFusionTitleIntoTimeline(self, titleName: str) -> TimelineItem:
        """ Inserts a Fusion title (indicated by titleName : string) into the timeline. """
        ...
    
    def GrabStill(self) -> GalleryStill:
        """ Grabs still from the current video clip. Returns a GalleryStill object. """
        ...

    def GrabAllStills(self, stillFrameSource: StillFrameSource) -> List[GalleryStill]:
        """
        Grabs stills from all the clips of the timeline at 'stillFrameSource' (1 - First frame, 2 - Middle frame).
        Returns the list of GalleryStill objects.
        """
        ...

    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the timeline """
        ...

    def CreateSubtitlesFromAudio(self, autoCaptionSettings: Optional[AutoCaptionSettings]) -> bool:
        """
        Creates subtitles from audio for the timeline.
        Takes in optional dictionary {autoCaptionSettings}. Check 'Auto Caption Settings' subsection below for more information.
        Returns True on success, False otherwise.
        """
        ...

    def DetectSceneCuts(self) -> bool:
        """ Detects and makes scene cuts along the timeline. Returns True if successful, False otherwise. """
        ...

    def ConvertTimelineToStereo(self) -> bool:
        """ Converts timeline to stereo. Returns True if successful; False otherwise. """
        ...

    def GetNodeGraph(self) -> Graph:
        """ Returns the timeline's node graph object. """
        ...

    def AnalyzeDolbyVision(self, timelineItems: Optional[List[TimelineItem]], analysisType = None) -> bool:
        """
        Analyzes Dolby Vision on clips present on the timeline. Returns True if analysis start is successful; False otherwise.
        if [timelineItems] is empty, analysis performed on all items. Else, analysis performed on [timelineItems] only.
        set analysisType to resolve.DLB_BLEND_SHOTS for blend setting.
        """


class TimelineItem:

    def GetName(self) -> str:
        """ Returns the item name. """
        ...

    def GetDuration(self, subframe_precision: bool) -> int | float:
        """ Returns the item duration. Returns fractional frames if subframe_precision is True. """
        ...

    def GetEnd(self, subframe_precision: bool)  -> int | float:
        """ Returns the end frame position on the timeline. Returns fractional frames if subframe_precision is True. """
        ...

    def GetSourceEndFrame(self) -> int:
        """ Returns the end frame position of the media pool clip in the timeline clip. """
        ...

    def GetSourceEndTime(self) -> float:
        """ Returns the end time position of the media pool clip in the timeline clip. """
        ...

    def GetFusionCompCount(self) -> int:
        """ Returns number of Fusion compositions associated with the timeline item. """
        ...

    def GetFusionCompByIndex(self, compIndex: int) -> FusionComp:
        """ Returns the Fusion composition object based on given index. 1 <= compIndex <= timelineItem.GetFusionCompCount() """
        ...

    def GetFusionCompNameList(self) -> List[str]:
        """ Returns a list of Fusion composition names associated with the timeline item. """
        ...

    @deprecated
    def GetFusionCompNames(self) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of Fusion composition names associated with the timeline item.
        """
        ...

    def GetFusionCompByName(self, compName: str) -> FusionComp:
        """ Returns the Fusion composition object based on given name. """
        ...

    def GetLeftOffset(self, subframe_precision: bool) -> int | float:
        """ Returns the maximum extension by frame for clip from left side. Returns fractional frames if subframe_precision is True. """
        ...

    def GetRightOffset(self, subframe_precision: bool) -> int | float:
        """ Returns the maximum extension by frame for clip from right side. Returns fractional frames if subframe_precision is True. """
        ...

    def GetStart(self, subframe_precision: bool) -> int | float:
        """ Returns the start frame position on the timeline. Returns fractional frames if subframe_precision is True. """
        ...

    def GetSourceStartFrame(self) -> int:
        """ Returns the start frame position of the media pool clip in the timeline clip. """
        ...

    def GetSourceStartTime(self) -> float:
        """ Returns the start time position of the media pool clip in the timeline clip. """
        ...

    def SetProperty(self, propertyKey: str, propertyValue: Any) -> bool:
        """
        Sets the value of property "propertyKey" to value "propertyValue".
        Refer to "Looking up Timeline item properties" for more information.
        """
        ...

    def GetProperty(self, propertyKey: Optional[str]) -> int | dict[str, str]:
        """
        Returns the value of the specified key.
        If no key is specified, the method returns a dictionary(python) or table(lua) for all supported keys.
        """
        ...

    def AddMarker(self, frameId: float, color: MarkerColor, name: str, note: str, duration: float, customData: Optional[str]) -> bool:
        """ 
        Creates a new marker at given frameId position and with given marker information.
        'customData' is optional and helps to attach user specific data to the marker. 
        """
        ...

    def GetMarkers(self) -> dict[float, Marker]:
        """
        Returns a dict (frameId -> {information}) of all markers and dicts with their information. 
        Example: a value of {96.0: {'color': 'Green', 'duration': 1.0, 'note': '', 'name': 'Marker 1', 'customData': ''}, ...} indicates a single green marker at clip offset 96
        """
        ...

    def GetMarkerByCustomData(self, customData: str) -> dict[float, Marker]:
        """ Returns marker {information} for the first matching marker with specified customData. """
        ...

    def UpdateMarkerCustomData(self, frameId: float, customData: str) -> bool:
        """ Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user specific data to markers. """
        ...

    def GetMarkerCustomData(self, frameId: float) -> str:
        """ Returns customData string for the marker at given frameId position. """
        ...

    def DeleteMarkersByColor(self, color: MarkerColor | Literal['All']) -> bool:
        """ Delete all markers of the specified color from the timeline item. "All" as argument deletes all color markers. """
        ...

    def DeleteMarkerAtFrame(self, frameNum: float) -> bool:
        """ Delete marker at frame number from the timeline item. """
        ...

    def DeleteMarkerByCustomData(self, customData: str) -> bool:
        """ Delete first matching marker with specified customData. """
        ...

    def AddFlag(self, color: FlagColor) -> bool:
        """ Adds a flag with given color (string). """
        ...

    def GetFlagList(self) -> List[FlagColor]:
        """ Returns a list of flag colors assigned to the item. """
        ...

    @deprecated
    def GetFlags(self) -> dict[Any, FlagColor]:
        """
        Deprecated!

        Returns a dict of flag colors assigned to the item.
        """
        ...

    def ClearFlags(self, color: FlagColor) -> bool:
        """ Clear flags of the specified color. An "All" argument is supported to clear all flags. """
        ...

    def GetClipColor(self) -> ClipColor:
        """ Returns the item color as a string. """
        ...

    def SetClipColor(self, colorName: ClipColor) -> bool:
        """ Sets the item color based on the colorName (string). """
        ...

    def ClearClipColor(self) -> bool:
        """ Clears the item color. """
        ...

    def AddFusionComp(self) -> FusionComp:
        """ Adds a new Fusion composition associated with the timeline item. """
        ...

    def ImportFusionComp(self, path: str) -> FusionComp:
        """ Imports a Fusion composition from given file path by creating and adding a new composition for the item. """
        ...

    def ExportFusionComp(self, path: str, compIndex: int) -> bool:
        """ Exports the Fusion composition based on given index to the path provided. """
        ...

    def DeleteFusionCompByName(self, compName: str) -> bool:
        """ Deletes the named Fusion composition. """
        ...

    def LoadFusionCompByName(self, compName: str) -> FusionComp:
        """ Loads the named Fusion composition as the active composition. """
        ...

    def RenameFusionCompByName(self, oldName: str, newName: str) -> bool:
        """ Renames the Fusion composition identified by oldName. """
        ...

    def AddVersion(self, versionName: str, versionType: VersionType) -> bool:
        """ Adds a new color version for a video clip based on versionType (0 - local, 1 - remote). """
        ...

    def GetCurrentVersion(self) -> dict[str, VersionType]:
        """ 
        Returns the current version of the video clip. 
        The returned value will have the keys versionName and versionType(0 - local, 1 - remote). 
        """
        ...

    def DeleteVersionByName(self, versionName: str, versionType: VersionType) -> bool:
        """ Deletes a color version by name and versionType (0 - local, 1 - remote). """
        ...

    def LoadVersionByName(self, versionName: str, versionType: VersionType) -> bool:
        """ Loads a named color version as the active version. versionType: 0 - local, 1 - remote. """
        ...

    def RenameVersionByName(self, oldName: str, newName: str, versionType: VersionType) -> bool:
        """ Renames the color version identified by oldName and versionType (0 - local, 1 - remote). """
        ...

    def GetVersionNameList(self, versionType: VersionType) -> List[str]:
        """ Returns a list of all color versions for the given versionType (0 - local, 1 - remote). """
        ...

    @deprecated
    def GetVersionNames(self, versionType) -> dict[Any, str]:
        """
        Deprecated!

        Returns a dict of version names by provided versionType: 0 - local, 1 - remote.
        """
        ...

    def GetMediaPoolItem(self) -> MediaPoolItem:
        """ Returns the media pool item corresponding to the timeline item if one exists. """
        ...

    def GetStereoConvergenceValues(self) -> dict[Any, Any]:
        """ Returns a dict (offset -> value) of keyframe offsets and respective convergence values. """
        ...

    def GetStereoLeftFloatingWindowParams(self) -> dict[Any, FloatingWindowParams]:
        """ 
        For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. 
        Value at particular offset includes the left, right, top and bottom floating window values. 
        """
        ...

    def GetStereoRightFloatingWindowParams(self) -> dict[Any, FloatingWindowParams]:
        """ 
        For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params. 
        Value at particular offset includes the left, right, top and bottom floating window values. 
        """
        ...

    @deprecated
    def GetNumNodes(self) -> int:
        """
        Deprecated!

        Returns the number of nodes in the current graph for the timeline item.
        """
        ...

    def ApplyArriCdlLut(self) -> bool:
        """ Applies ARRI CDL and LUT. Returns True if successful, False otherwise. """
        ...

    @deprecated
    def SetLUT(self, nodeIndex: int, lutPath: str) -> bool:
        """
        Deprecated!

        Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <= total number of nodes.
        The lutPath can be an absolute path, or a relative path (based off custom LUT paths or the master LUT path).
        The operation is successful for valid lut paths that Resolve has already discovered (see Project.RefreshLUTList).
        """
        ...

    @deprecated
    def GetLUT(self, nodeIndex: int) -> str:
        """
        Deprecated!

        Gets relative LUT path based on the node index provided, 1 <= nodeIndex <= total number of nodes.
        """
        ...

    def SetCDL(self, cdlMap: CDLMap) -> bool:
        """
        Keys of map are: "NodeIndex", "Slope", "Offset", "Power", "Saturation", where 1 <= NodeIndex <= total number of nodes.
        Example python code - SetCDL({"NodeIndex" : "1", "Slope" : "0.5 0.4 0.2", "Offset" : "0.4 0.3 0.2", "Power" : "0.6 0.7 0.8", "Saturation" : "0.65"})
        """
        ...

    def AddTake(self, mediaPoolItem: MediaPoolItem, startFrame: Optional[int], endFrame: Optional[int]) -> bool:
        """
        Adds mediaPoolItem as a new take. Initializes a take selector for the timeline item if needed.
        By default, the full clip extents is added. startFrame (int) and endFrame (int) are optional arguments used to specify the extents.
        """
        ...

    def GetSelectedTakeIndex(self) -> int:
        """ Returns the index of the currently selected take, or 0 if the clip is not a take selector. """
        ...

    def GetTakesCount(self) -> int:
        """ Returns the number of takes in take selector, or 0 if the clip is not a take selector. """
        ...

    def GetTakeByIndex(self, idx: int) -> TakeInfo:
        """ Returns a dict (keys "startFrame", "endFrame" and "mediaPoolItem") with take info for specified index. """
        ...

    def DeleteTakeByIndex(self, idx: int) -> bool:
        """ Deletes a take by index, 1 <= idx <= number of takes. """
        ...

    def SelectTakeByIndex(self, idx: int) -> bool:
        """ Selects a take by index, 1 <= idx <= number of takes. """
        ...

    def FinalizeTake(self) -> bool:
        """ Finalizes take selection. """
        ...

    def CopyGrades(self, tgtTimelineItems: List[TimelineItem]) -> bool:
        """
        Copies the current node stack layer grade to the same layer for each item in tgtTimelineItems.
        Returns True if successful.
        """
        ...

    def SetClipEnabled(self, Bool: bool) -> bool:
        """ Sets clip enabled based on argument. """
        ...

    def GetClipEnabled(self) -> bool:
        """ Gets clip enabled status. """
        ...

    def UpdateSidecar(self) -> bool:
        """ Updates sidecar file for BRAW clips or RMD file for R3D clips. """
        ...

    def GetUniqueId(self) -> str:
        """ Returns a unique ID for the timeline item """
        ...

    def LoadBurnInPreset(self, presetName: str) -> bool:
        """ Loads user defined data burn in preset for clip when supplied presetName (string). Returns true if successful. """
        ...

    @deprecated
    def GetNodeLabel(self, nodeIndex: int) -> str:
        """
        Deprecated!

        Returns the label of the node at nodeIndex.
        """
        ...

    def CreateMagicMask(self, mode: MagicMaskMode) -> bool:
        """ Returns True if magic mask was created successfully, False otherwise. mode can "F" (forward), "B" (backward), or "BI" (bidirection) """
        ...

    def RegenerateMagicMask(self) -> bool:
        """ Returns True if magic mask was regenerated successfully, False otherwise. """
        ...

    def Stabilize(self) -> bool:
        """ Returns True if stabilization was successful, False otherwise """
        ...

    def SmartReframe(self) -> bool:
        """ Performs Smart Reframe. Returns True if successful, False otherwise. """
        ...

    def GetNodeGraph(self, layerIdx: Optional[int]) -> Graph:
        """
        Returns the clip's node graph object at layerIdx (int, optional).
        Returns the first layer if layerIdx is skipped. 1 <= layerIdx <= project.GetSetting("nodeStackLayers").
        """
        ...

    def GetColorGroup(self) -> ColorGroup:
        """ Returns the clip's color group if one exists. """
        ...

    def AssignToColorGroup(self, colorGroup: ColorGroup) -> bool:
        """
        Returns True if TiItem to successfully assigned to given ColorGroup.
        ColorGroup must be an existing group in the current project.
        """
        ...

    def RemoveFromColorGroup(self) -> bool:
        """ Returns True if the TiItem is successfully removed from the ColorGroup it is in. """
        ...

    def ExportLUT(self, exportType: LUTExportType, path: str) -> bool:
        """
        Exports LUTs from tiItem referring to value passed in 'exportType' (enum) for LUT size. Refer to. 'ExportLUT notes' section for possible values.
        Saves generated LUT in the provided 'path' (string). 'path' should include the intended file name.
        If an empty or incorrect extension is provided, the appropriate extension (.cube/.vlt) will be appended at the end of the path.
        """
        ...

    def GetLinkedItems(self) -> List[TimelineItem]:
        """ Returns a list of linked timeline items. """
        ...

    def GetTrackTypeAndIndex(self) -> tuple[TrackType, int]:
        """
        Returns a list of two values that correspond to the TimelineItem's trackType (string) and trackIndex (int) respectively.
        trackType is one of {"audio", "video", "subtitle"}
        1 <= trackIndex <= Timeline.GetTrackCount(trackType)
        """

    def GetSourceAudioChannelMapping(self) -> str:
        """
        Returns a string with TimelineItem's audio mapping information.
        Check 'Audio Mapping' section below for more information.
        """
        ...


class Gallery:

    def GetAlbumName(self, galleryStillAlbum: GalleryStillAlbum) -> str:
        """ Returns the name of the GalleryStillAlbum object 'galleryStillAlbum'. """
        ...

    def SetAlbumName(self, galleryStillAlbum: GalleryStillAlbum, albumName: str) -> bool:
        """ Sets the name of the GalleryStillAlbum object 'galleryStillAlbum' to 'albumName'. """
        ...

    def GetCurrentStillAlbum(self) -> GalleryStillAlbum:
        """ Returns current album as a GalleryStillAlbum object. """
        ...

    def SetCurrentStillAlbum(self, galleryStillAlbum: GalleryStillAlbum) -> bool:
        """ Sets current album to GalleryStillAlbum object 'galleryStillAlbum'. """
        ...

    def GetGalleryStillAlbums(self) -> List[GalleryStillAlbum]:
        """ Returns the gallery albums as a list of GalleryStillAlbum objects. """
        ...


class GalleryStillAlbum:

    def GetStills(self) -> List[GalleryStill]:
        """ Returns the list of GalleryStill objects in the album. """
        ...

    def GetLabel(self, galleryStill: GalleryStill) -> str:
        """ Returns the label of the galleryStill. """
        ...

    def SetLabel(self, galleryStill: GalleryStill, label: str) -> bool:
        """ Sets the new 'label' to GalleryStill object 'galleryStill'. """
        ...

    def ImportStills(self, filePaths: List[str]) -> bool:
        """ Imports GalleryStill from each filePath in [filePaths] list. True if at least one still is imported successfully. False otherwise. """
        ...

    def ExportStills(self, galleryStills: List[GalleryStill], folderPath: str, filePrefix: str, format: GalleryStillExportFormat) -> bool:
        """
        Exports list of GalleryStill objects '[galleryStill]' to directory 'folderPath', with filename prefix 'filePrefix',
        using file format 'format' (supported formats: dpx, cin, tif, jpg, png, ppm, bmp, xpm, drx).
        """

    def DeleteStills(self, galleryStills: List[GalleryStill]) -> bool:
        """ Deletes specified list of GalleryStill objects '[galleryStill]'. """
        ...


class GalleryStill:
    """ This class does not provide any API functions but the object type is used by functions in other classes. """
    pass


class Graph:

    def GetNumNodes(self) -> int:
        """ Returns the number of nodes in the graph """
        ...

    def SetLUT(self, nodeIndex: int, lutPath: str) -> bool:
        """
        Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <= self.GetNumNodes().
        The lutPath can be an absolute path, or a relative path (based off custom LUT paths or the master LUT path).
        The operation is successful for valid lut paths that Resolve has already discovered (see Project.RefreshLUTList).
        """
        ...

    def GetLUT(self, nodeIndex: int) -> str:
        """ Gets relative LUT path based on the node index provided, 1 <= nodeIndex <= total number of nodes. """
        ...

    def GetNodeLabel(self, nodeIndex: int) -> str:
        """ Returns the label of the node at nodeIndex. """
        ...

    def GetToolsInNode(self, nodeIndex: int) -> List[str]:
        """ Returns toolsList (list of strings) of the tools used in the node indicated by given nodeIndex (int). """
        ...

    def SetNodeEnabled(self, nodeIndex: int, isEnabled: bool) -> bool:
        """
        Sets the node at the given nodeIndex (int) to isEnabled (bool).
        1 <= nodeIndex <= self.GetNumNodes().
        """
        ...


class ColorGroup:

    def GetName(self) -> str:
        """ Returns the name (string) of the ColorGroup. """
        ...

    def SetName(self, groupName: str) -> bool:
        """ Renames ColorGroup to groupName (string). """
        ...

    def GetClipsInTimeline(self, timeline: Optional[Timeline]) -> List[TimelineItem]:
        """
        Returns a list of TimelineItem that are in colorGroup in the given Timeline.
        Timeline is Current Timeline by default.
        """
        ...

    def GetPreClipNodeGraph(self) -> Graph:
        """ Returns the ColorGroup Pre-clip graph. """
        ...

    def GetPostClipNodeGraph(self) -> Graph:
        """ Returns the ColorGroup Post-clip graph. """
        ...


class Fusion:
    """ No documentation available """
    pass


class FusionComp:
    """ No documentation available """
    pass
